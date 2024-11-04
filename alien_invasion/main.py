# UNFINISHED
import sys
import pygame
from sprites import *
from enemy import *
from bullet import Bullet
from config import Settings


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

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self.player.update()
            self._update_bullets()

    def _check_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                sys.exit()
            if keys[pygame.K_SPACE]:
                self._fire_bullet()

    def _fire_bullet(self):
        # Firing a bullet; if it exceed a certain limit,
        # new bullets cannot be fired
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # Removing bullets when they leave the screen
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

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

    def _create_enemy(self, x_position, y_position):
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.enemies.add(new_enemy)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        self.enemies.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()