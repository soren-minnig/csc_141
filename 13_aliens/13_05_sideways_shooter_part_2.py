# 3: I felt moderately confident with this program
import sys
import pygame
from pygame.sprite import Sprite
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
                self.y -= 3
        if keys[pygame.K_s]:
             self.moving_down = True
             if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.y += 3

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.color = (227, 186, 75)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = game.player.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += 2.0
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load('13_aliens/img/enemy_sideways.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x -= 1
        self.rect.x = self.x

    def check_edge(self):
        # Checking if the raindrop has left the screen
        screen_rect = self.screen.get_rect()
        return (self.rect.right <= screen_rect.left)


class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (1200, 800))
        
        # A pleasant light blue, how dandy...
        self.bg_color = (116, 181, 194)
        pygame.display.set_caption('Sideways Shooter')

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # An enemy spawns every 3.5 seconds
        pygame.time.set_timer(pygame.USEREVENT, 3500)

    def run_game(self):
        # Run the game
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self.player.update()
            self._update_bullets()
            self._update_enemy()

    def _check_events(self):
        keys = pygame.key.get_pressed()
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                sys.exit()
            if keys[pygame.K_SPACE]:
                self._fire_bullet()
            if event.type == pygame.USEREVENT:
                self._spawn_enemy()

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
                # There's no game over, so we'll get rid of the enemy when
                # they reach the left side
                self.enemies.remove(enemy)

    def _update_screen(self):
        # Update images on screen
        self.screen.fill(self.bg_color)
        self.player.blitme()
        self.enemies.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()


if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()