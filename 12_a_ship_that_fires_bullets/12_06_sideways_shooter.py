import sys
import pygame
from pygame.sprite import Sprite


# I mostly copy-and-pasted my own code and changed parts of it so
# the player can move up and down and the bullets move left to right
class Player:
    # Class to draw the rocket
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('12_a_ship_that_fires_bullets/img/sideways.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

     # Storing the rocket's horizontal position
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
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = (227, 186, 75)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_game.player.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += 2.0
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


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

    def run_game(self):
        # Run the game
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self.player.update()
            self._update_bullets()

    def _check_events(self):
        keys = pygame.key.get_pressed()
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                sys.exit()
            if keys[pygame.K_SPACE]:
                self._fire_bullet()

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

    def _update_screen(self):
        # Update images on screen
        self.screen.fill(self.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()


if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()