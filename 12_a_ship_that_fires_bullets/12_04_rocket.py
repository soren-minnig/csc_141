import sys
import pygame


class Rocket:
    # Class to draw the rocket
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('12_a_ship_that_fires_bullets/img/placeholder.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.center

     # Storing the rocket's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.movement()

        self.rect.x = self.x
        self.rect.y = self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moving_left = True
            if self.moving_left and self.rect.left > 0:
                self.x -= 3
        if keys[pygame.K_d]:
             self.moving_right = True
             if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += 3
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


class RocketGame:
    # Class to run the game
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (1200, 800))
        
        # A pleasant light blue, how dandy...
        self.bg_color = (116, 181, 194)
        pygame.display.set_caption('Rocket Game')

        self.rocket = Rocket(self)

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
        self.rocket.blitme()
        self.rocket.update()
        
        pygame.display.flip()


if __name__ == '__main__':
    game = RocketGame()
    game.run_game()