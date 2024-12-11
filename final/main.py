### Credits ###
# Music from Sonic Mania
# Gunshot and death SFX from Metal Gear Solid
# Bomb laugh SFX from Super Mario 64
# Bomb explosion SFX is...a stock sound effect...from somewhere...
# ^ (It appears in Deltarune, which is where I first heard it)
# Game font from Minecraft
# All sprites are original, but I referenced B&W walk cycles to animate the enemies!


import sys
import json
from pathlib import Path
import pygame
from time import sleep
from random import randint
from sprites import Player
from enemy import Enemy
from enemy import BombEnemy
from background import Background
from bullet import Bullet
from bullet import EnemyBullet
from button import Button
from difficulty import DifficultyButton
from config import Settings
from stats import Stats
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (832, 960))
        icon = pygame.image.load('final/img/bomb.png')
        
        pygame.display.set_caption('Ghost Town')
        pygame.display.set_icon(icon)
        
        self.settings = Settings()
        self.stats = Stats(self)
        self.sb = Scoreboard(self)

        self.map = Background(self)

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Buttons
        self.start_button = Button(self, 'Start')
        self.easy_button = DifficultyButton(self, 416, 400, (0, 135, 0), 'Easy')
        self.medium_button = DifficultyButton(self, 416, 500, (255, 194, 41), 'Medium')
        self.hard_button = DifficultyButton(self, 416, 600, (219, 0, 22), 'Hard')

        # Music
        pygame.mixer_music.load('final/sfx/music.mp3')

        # SFX
        self.shoot_sound = pygame.mixer.Sound('final/sfx/gunshot.wav')
        self.empty_sound = pygame.mixer.Sound('final/sfx/gun_empty.wav')
        self.laugh_sound = pygame.mixer.Sound('final/sfx/bomb_laugh.mp3')
        self.explode_sound = pygame.mixer.Sound('final/sfx/explosion.mp3')

        sounds = [self.shoot_sound, self.empty_sound, self.laugh_sound,
                  self.explode_sound]

        # Volume
        pygame.mixer_music.set_volume(0.03)
        for sound in sounds:
            sound.set_volume(0.03)

        self.game_active = False
        self.difficulty_chosen = False

        self.difficulty = ''
        self.counter = 0

        pygame.time.set_timer(pygame.USEREVENT, 3500)

    def run_game(self):
        # Run the game
        while True:
            self._check_events()
        
            if self.game_active:
                # self.map.update()
                self.player.update()
                self._update_bullets()
                self._update_enemy_bullets()
                self._update_enemy()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        keys = pygame.key.get_pressed()
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                self._save_high_score()
                sys.exit()
            if keys[pygame.K_SPACE] and self.game_active:
                self._fire_bullet()
            if event.type == pygame.USEREVENT:
                if self.game_active:
                    self._spawn_enemy()
                    self.counter += 1
                    if self.counter % 4 == 0:
                        # If the number of enemies spawned is divisible by 4,
                        # speed them up
                        self.settings.increase_speed()
                        print("Speedup")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_start_button(mouse_pos)
                self._check_difficulty_button(mouse_pos)

    def _player_hit(self):
        if self.stats.lives_left > 0:
            self.stats.lives_left -= 1
            self.sb.prep_lives()

            self.bullets.empty()
            self.enemies.empty()

            if self.difficulty == 'easy':
                self.settings.initialize_easy_dynamic_settings()
            if self.difficulty == 'medium':
                self.settings.initialize_medium_dynamic_settings()
            if self.difficulty == 'hard':
                self.settings.initialize_hard_dynamic_settings()

            sleep(0.5)
        else:
            self.restart_game()
    
    def _fire_bullet(self):
        # Firing a bullet; if it exceed a certain limit,
        # new bullets cannot be fired
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
            pygame.mixer.Channel(1).play(self.shoot_sound)

        pygame.mixer.Sound.play(self.empty_sound)

    def _update_bullets(self):
        self.bullets.update()

        # Removing bullets when they leave the screen
        for bullet in self.bullets.copy():
                if bullet.rect.top <= 0:
                    self.bullets.remove(bullet)

        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        for enemy in self.enemies:
            for bullet in self.bullets:
                collisions = pygame.sprite.collide_rect(
                    bullet, enemy)

                if collisions:
                    self.bullets.remove(bullet)
                    if enemy.type == 3:
                        enemy.exploding = True
                    else:
                        self.enemies.remove(enemy)
                    self.stats.score += self.settings.enemy_points
                    self.sb.prep_score()
                    self.sb.check_high_score()

    def _update_enemy_bullets(self):
        self.enemy_bullets.update()

        for bullet in self.enemy_bullets.copy():
            if bullet.rect.top >= 960:
                self.enemy_bullets.remove(bullet)
        
        self._check_enemy_bullet_collisions()

    def _check_enemy_bullet_collisions(self):
        for bullet in self.enemy_bullets:
            collisions = pygame.sprite.collide_rect(
                bullet, self.player)
            if collisions:
                self.enemy_bullets.remove(bullet)
                self._player_hit()

    def _create_enemy(self, x_position, y_position):
        enemy_type = randint(1, 3)
        # enemy_type = 3 # Bomb enemy debugging
        if enemy_type == 1 or 2:
            new_enemy = Enemy(self, enemy_type)
        if enemy_type == 3:
            new_enemy = BombEnemy(self)
        new_enemy.x = x_position
        new_enemy.y = y_position
        new_enemy.rect.x = new_enemy.x
        new_enemy.rect.y = new_enemy.y
        self.enemies.add(new_enemy)

    def _spawn_enemy(self):
        lane = randint(1, 11)
        x_position = lane * 64
        self._create_enemy(x_position, 0)
        # print(lane)  # Debugging

    def _update_enemy(self):
        self.enemies.update()
        for enemy in self.enemies.sprites():
            if enemy.type == 1 and (self.player.rect.x - enemy.rect.x <= 32 and self.player.rect.x - enemy.rect.x >= -32):
                if len(self.enemy_bullets) < 1:
                    new_bullet = EnemyBullet(self, enemy.rect.midbottom)
                    self.enemy_bullets.add(new_bullet)

                    pygame.mixer.Sound.play(self.shoot_sound)
            if enemy.type == 3 and (self.player.rect.x - enemy.rect.x <= 32 and self.player.rect.x - enemy.rect.x >= -32):
                enemy.running = True
            if enemy.type == 3 and enemy.running == True:
                if not enemy.exploding:
                    pygame.mixer.Sound.play(self.laugh_sound)
            if enemy.check_edge():
                self.enemies.remove(enemy)
                self._player_hit()
                # print("method 1")  # Debugging
            if pygame.sprite.spritecollide(self.player, self.enemies, True):
                self._player_hit()
                # print("method 2")  # Debugging

    def _check_start_button(self, mouse_pos):
        if self.start_button.rect.collidepoint(mouse_pos) and not self.game_active:
            if self.difficulty_chosen:
                self.start()

    def _check_difficulty_button(self, mouse_pos):
        if self.easy_button.rect.collidepoint(mouse_pos) and not self.difficulty_chosen:
            self.settings.initialize_easy_dynamic_settings()
            self.difficulty_chosen = True
            self.difficulty = 'easy'
        if self.medium_button.rect.collidepoint(mouse_pos) and not self.difficulty_chosen:
            self.settings.initialize_medium_dynamic_settings()
            self.difficulty_chosen = True
            self.difficulty = 'medium'
        if self.hard_button.rect.collidepoint(mouse_pos) and not self.difficulty_chosen:
            self.settings.initialize_hard_dynamic_settings()
            self.difficulty_chosen = True
            self.difficulty = 'hard'

    def start(self):
        self.stats.reset_stats()
        self.sb.prep_images()
        self.game_active = True

        self.bullets.empty()
        self.enemy_bullets.empty()
        self.enemies.empty()

        pygame.mixer_music.play(-1)

        pygame.mouse.set_visible(False)

    def restart_game(self):
        self.difficulty = ''
        self.difficulty_chosen = False
        self.game_active = False
        pygame.mouse.set_visible(True)
        pygame.mixer.music.stop()

    def _save_high_score(self):
        saved_high_score = self.stats.check_high_score()
        if self.stats.high_score > saved_high_score:
            path = Path('game_high_score.json')
            contents = json.dumps(self.stats.high_score)
            path.write_text(contents)
    
    def _update_screen(self):
        # Update images on screen
        self.map.blitme()
        self.player.blitme()
        self.enemies.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for enemy_bullet in self.enemy_bullets.sprites():
            enemy_bullet.draw_bullet()

        self.sb.show_score()

        if not self.game_active:
            if not self.difficulty_chosen:
                self.easy_button.draw_button()
                self.medium_button.draw_button()
                self.hard_button.draw_button()
            if self.difficulty_chosen:
                self.start_button.draw_button()
        
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()