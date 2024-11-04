# UNFINISHED
import pygame
from pygame import Sprite

class Star(Sprite):
    def __init__(self):
        def __init__(self, game):
            super().__init__()
            self.screen = game.screen

            self.image = pygame.image.load('')
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
        pygame.display.set_caption('Starry Night')

        self.stars = pygame.sprite.Group()
        self._create_sky()

    def run_game(self):
        self._update_screen()

    def _create_sky(self):
        star = Star(self)
        self.stars.add(star)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < ( - 3 * star_height):
            while current_x < (1200 - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        self.screen.fill(self.bg_color)

if __name__ == '__main__':
    game = StarryNight()
    game.run_game()