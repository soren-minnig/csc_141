# 1: simple
import sys
import pygame


class BlueSky:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (1200, 800))
        
        # A pleasant light blue, how dandy...
        self.bg_color = (116, 181, 194)
        pygame.display.set_caption('Blue Sky')

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
        
        pygame.display.flip()


if __name__ == '__main__':
    game = BlueSky()
    game.run_game()