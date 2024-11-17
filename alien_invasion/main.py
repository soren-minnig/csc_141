# Should be fully operable but I will make visual changes later
import sys
import json
from pathlib import Path
import pygame
from time import sleep
from sprites import Player
from enemy import Enemy
from bullet import Bullet
from button import Button
from difficulty import DifficultyButton
from config import Settings
from stats import Stats
from scoreboard import Scoreboard


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
            self.settings.screen_height)
        )

        # Fullscreen code
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        # Stats
        self.stats = Stats(self)
        self.sb = Scoreboard(self)

        # Sprites
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Internal
        self.difficulty_chosen = False
        self.game_active = False
        self._create_fleet()

        # Buttons
        self.start_button = Button(self, 'Start')
        self.easy_button = DifficultyButton(self, 600, 300, (0, 135, 0), 'Easy')
        self.medium_button = DifficultyButton(self, 600, 400, (255, 194, 41), 'Medium')
        self.hard_button = DifficultyButton(self, 600, 500, (219, 0, 22), 'Hard')

        # SFX (from Sonic)
        self.shoot_sound = pygame.mixer.Sound('alien_invasion/sfx/S1_AB.wav')
        self.enemy_defeat_sound = pygame.mixer.Sound('alien_invasion/sfx/S1_AC.wav')

        # Volume
        self.shoot_sound.set_volume(0.25)
        self.enemy_defeat_sound.set_volume(0.1)

    def run_game(self):
        while True:
            self._check_events()
        
            if self.game_active:
                self.player.update()
                self._update_bullets()
                self._update_enemies()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                self.end_game()
            if keys[pygame.K_p]:
                if self.game_active == False:
                    self.start()
            if keys[pygame.K_r]:
                if self.game_active == True:
                    self.restart_game()
            if keys[pygame.K_SPACE]:
                self._fire_bullet()
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

            self._create_fleet()
            self.player.center_player()

            sleep(0.5)
        else:
            self.restart_game()

    def _fire_bullet(self):
        # Firing a bullet; if it exceed a certain limit,
        # new bullets cannot be fired
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
            pygame.mixer.Sound.play(self.shoot_sound)

    def _update_bullets(self):
        self.bullets.update()

        # Removing bullets when they leave the screen
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.enemies, True, True)
        
        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.sb.prep_score()
            self.sb.check_high_score()

            pygame.mixer.Sound.play(self.enemy_defeat_sound)
        
        if not self.enemies:
            self.start_new_level()

    def _create_fleet(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)
        enemy_width, enemy_height = enemy.rect.size

        current_x, current_y = enemy_width, enemy_height
        while current_y < (self.settings.screen_height - 3 * enemy_height):
            while current_x < (self.settings.screen_width - 2 * enemy_width):
                self._create_enemy(current_x, current_y)
                current_x += 2 * enemy_width

            current_x = enemy_width
            current_y += 2 * enemy_height

    def _check_fleet_edges(self):
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_enemy(self, x_position, y_position):
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.enemies.add(new_enemy)

    def _update_enemies(self):
        self._check_fleet_edges()
        self.enemies.update()

        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self._player_hit()

        self._check_enemies_bottom()

    def _check_enemies_bottom(self):
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= self.settings.screen_height:
                self._player_hit()
                break

    def _check_difficulty_button(self, mouse_pos):
        if self.easy_button.rect.collidepoint(mouse_pos) and not self.difficulty_chosen:
            self.settings.initialize_easy_dynamic_settings()
            self.difficulty_chosen = True
        if self.medium_button.rect.collidepoint(mouse_pos) and not self.difficulty_chosen:
            self.settings.initialize_medium_dynamic_settings()
            self.difficulty_chosen = True
        if self.hard_button.rect.collidepoint(mouse_pos) and not self.difficulty_chosen:
            self.settings.initialize_hard_dynamic_settings()
            self.difficulty_chosen = True

    def _check_start_button(self, mouse_pos):
        if self.start_button.rect.collidepoint(mouse_pos) and not self.game_active:
            if self.difficulty_chosen:
                self.start()

    def start(self):
        self.stats.reset_stats()
        self.sb.prep_images()
        self.game_active = True

        self.bullets.empty()
        self.enemies.empty()

        self._create_fleet()
        self.player.center_player()

        pygame.mouse.set_visible(False)

    def start_new_level(self):
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        self.stats.level += 1
        self.sb.prep_level()

    def _save_high_score(self):
        saved_high_score = self.stats.check_high_score()
        if self.stats.high_score > saved_high_score:
            path = Path('high_score.json')
            contents = json.dumps(self.stats.high_score)
            path.write_text(contents)

    def restart_game(self):
        self.difficulty_chosen = False
        self.game_active = False
        pygame.mouse.set_visible(True)

    def end_game(self):
        self._save_high_score()
        
        sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.enemies.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

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
    game = AlienInvasion()
    game.run_game()