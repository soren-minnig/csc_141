# 3: I actually prefer the way this plays over the final project
import sys
import json
from pathlib import Path
from time import sleep
import pygame
import pygame.font
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint


class Player:
    # Class to draw the player
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('12_a_ship_that_fires_bullets/img/sideways.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

     # Storing the player's horizontal position
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.movement()
        self.blitme()

        self.rect.y = self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.moving_up = True
            if self.moving_up and self.rect.top > 0:
                self.y -= 5
        if keys[pygame.K_s]:
             self.moving_down = True
             if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.y += 5

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Life(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load('14_scoring/img/life.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = (227, 186, 75)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = game.player.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += game.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('13_aliens/img/enemy_sideways.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x -= game.settings.enemy_speed
        self.rect.x = self.x

    def check_edge(self):
        # Checking if the raindrop has left the screen
        screen_rect = self.screen.get_rect()
        return (self.rect.right <= screen_rect.left)
    

class Settings:
    def __init__(self):
        # Player settings
        self.life_limit = 3

        # Speeding up the game
        self.speedup_scale = 1.1
        # Increasing point values
        self.score_scale = 1.5

    def initialize_easy_dynamic_settings(self):
        self.bullet_speed = 4
        self.enemy_speed = 1
        self.enemy_points = 50

    def initialize_medium_dynamic_settings(self):
        self.bullet_speed = 4.5
        self.enemy_speed = 1.5
        self.enemy_points = 60

    def initialize_hard_dynamic_settings(self):
        self.bullet_speed = 5
        self.enemy_speed = 2
        self.enemy_points = 70

    def increase_speed(self):
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)
    

class Stats:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        self.high_score = self.check_high_score()

    def reset_stats(self):
        self.lives_left = self.settings.life_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        path = Path('sideways_high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0
        

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30, 30, 30)
        self.bg_color = (116, 181, 194)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_lives()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score}"
        self.score_image = self.font.render(score_str, True,
                    self.text_color, self.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                        self.text_color, self.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_lives(self):
        self.lives = Group()
        for life_number in range(self.stats.lives_left):
            life = Life(self.game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class DifficultyButton:
    def __init__(self, game, x, y, color, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.x, self.y = x, y
        self.width, self.height = 200, 50
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (1200, 800))
        
        # A pleasant light blue, how dandy...
        self.bg_color = (116, 181, 194)
        pygame.display.set_caption('Sideways Shooter')

        self.settings = Settings()
        self.stats = Stats(self)
        self.sb = Scoreboard(self)

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.start_button = Button(self, 'Start')
        self.easy_button = DifficultyButton(self, 600, 300, (0, 135, 0), 'Easy')
        self.medium_button = DifficultyButton(self, 600, 400, (255, 194, 41), 'Medium')
        self.hard_button = DifficultyButton(self, 600, 500, (219, 0, 22), 'Hard')

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
                self.player.update()
                self._update_bullets()
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
            if keys[pygame.K_SPACE]:
                self._fire_bullet()
            if event.type == pygame.USEREVENT:
                if self.game_active:
                    self._spawn_enemy()
                    self.counter += 1
                    if self.counter % 4 == 0:
                        # If the number of enemies spawned is divisible by 4,
                        # speed them up
                        self.settings.increase_speed()
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

    def _update_bullets(self):
        self.bullets.update()

        # Removing bullets when they leave the screen
        for bullet in self.bullets.copy():
                if bullet.rect.left >= 1200:
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

    def _create_enemy(self, x_position, y_position):
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.enemies.add(new_enemy)

    def _spawn_enemy(self):
        lane = randint(1, 11)
        y_position = lane * 64
        self._create_enemy(1200, y_position)

    def _update_enemy(self):
        self.enemies.update()
        for enemy in self.enemies.sprites():
            if enemy.check_edge():
                self.enemies.remove(enemy)
                self._player_hit()
            if pygame.sprite.spritecollide(self.player, self.enemies, True):
                self._player_hit()

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
        self.enemies.empty()

        pygame.mouse.set_visible(False)

    def restart_game(self):
        self.difficulty = ''
        self.difficulty_chosen = False
        self.game_active = False
        pygame.mouse.set_visible(True)

    def _save_high_score(self):
        saved_high_score = self.stats.check_high_score()
        if self.stats.high_score > saved_high_score:
            path = Path('sideways_high_score.json')
            contents = json.dumps(self.stats.high_score)
            path.write_text(contents)
    
    def _update_screen(self):
        # Update images on screen
        self.screen.fill(self.bg_color)
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
    game = SidewaysShooter()
    game.run_game()