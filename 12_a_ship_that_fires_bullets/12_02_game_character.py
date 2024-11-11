# 1: simple
import sys
import pygame


class Character:
    # Class to draw the character
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('12_a_ship_that_fires_bullets/img/placeholder.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class GameCharacter:
    # Class to run the game
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (1200, 800))
        
        # A pleasant light blue, how dandy...
        self.bg_color = (116, 181, 194)
        pygame.display.set_caption('Game Character')

        self.character = Character(self)

    def run_game(self):
        # Run the game
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Update images on screen
        self.screen.fill(self.bg_color)
        self.character.blitme()
        
        pygame.display.flip()


if __name__ == '__main__':
    game = GameCharacter()
    game.run_game()