# 3: easy to figure out
import sys
import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Creating the raindrops
        self.image = pygame.image.load('13_aliens/img/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edge(self):
        # Checking if the raindrop has left the screen
        screen_rect = self.screen.get_rect()
        return (self.rect.top >= screen_rect.bottom)


class RainyNight:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (27, 40, 66)
        pygame.display.set_caption('Steady Rainy Night')

        self.raindrops = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        while True:
            self.clock.tick(60)
            self._check_events()
            self._update_screen()
            self._update_rain()

    def _check_events(self):
        keys = pygame.key.get_pressed()
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

    def _create_sky(self):
        raindrop = Raindrop(self)
        self.raindrops.add(raindrop)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (800 - 1 * raindrop_height):
            while current_x < (1200 - 2 * raindrop_width):
                self._create_rain(current_x, current_y)
                current_x += 2 * raindrop_width

            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _check_rain_edges(self):
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edge():
                current_x = raindrop.rect.x
                self.raindrops.remove(raindrop)
                self._create_rain(current_x, 32)
                break
        
    def _create_rain(self, x_position, y_position):
        new_raindrop = Raindrop(self)
        new_raindrop.x = x_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)

    def _update_rain(self):
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += 1
        self._check_rain_edges()


if __name__ == '__main__':
    game = RainyNight()
    game.run_game()