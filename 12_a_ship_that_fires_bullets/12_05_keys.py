import sys
import pygame


class Keys:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (1200, 800))
        
        # A pleasant light blue, how dandy...
        self.bg_color = (250, 250, 250)
        pygame.display.set_caption('Keys')

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
            elif event.type == pygame.KEYDOWN:
                # It prints different numbers for each key! "a" is 97, and it
                # increases for each letter of the alphabet after that
                print(event.key)
            

    def _update_screen(self):
        # Update images on screen
        self.screen.fill(self.bg_color)
        
        pygame.display.flip()


if __name__ == '__main__':
    game = Keys()
    game.run_game()