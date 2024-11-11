# 5: was a bit challenging to figure out how I should adjust the original
import sys
import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Creating the stars :3
        self.image = pygame.image.load('13_aliens/img/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


class StarryNight:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (27, 40, 66)
        pygame.display.set_caption('Better Starry Night')

        self.stars = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        while True:
            self.clock.tick(60)
            self._check_events()
            self._update_screen()

    def _check_events(self):
        keys = pygame.key.get_pressed()
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

    def _create_sky(self):
        star = Star(self)
        self.stars.add(star)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (800 - 1 * star_height):
            while current_x < (1200 - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += randint(128, 256)

            current_x = randint(32, 128)
            current_y += randint(64, 96)

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)


if __name__ == '__main__':
    game = StarryNight()
    game.run_game()