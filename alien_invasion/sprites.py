import pygame
from config import Settings

class Player:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load('alien_invasion/img/player.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Storing the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        self.movement()

        self.rect.x = self.x

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moving_left = True
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.player_speed
        if keys[pygame.K_d]:
             self.moving_right = True
             if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.player_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_player(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)