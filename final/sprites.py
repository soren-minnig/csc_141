import pygame
from pygame.sprite import Sprite
from config import Settings
import math


class Spritesheet(object):
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey((0, 0, 0))
        return image
    

class Player(Sprite):
    # Class to draw the player
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self._layer = 1

        self.image = pygame.image.load('final/img/player.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Storing the player's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.x_change = 0

        self.moving_left = False
        self.moving_right = False

        # Animation
        self.animation_loop = 0

    def update(self):
        self.movement()
        self.animate()
        self.blitme()

        self.rect.x += self.x_change

        self.x_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moving_left = True
            self.moving_right = False
            if self.moving_left and self.rect.left > 0:
                self.x_change -= 5
        if keys[pygame.K_d]:
             self.moving_right = True
             self.moving_left = False
             if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x_change += 5

    def animate(self):
        left_animations = [
            pygame.image.load('final/img/player.png'),
            pygame.image.load('final/img/player_2.png'),
            ]
        right_animations = [
            pygame.image.load('final/img/player.png'),
            pygame.image.load('final/img/player_3.png'),
            ]

        if self.moving_left == True:
            self.moving_right = False
            if self.x_change == 0:
                self.image = left_animations[0]
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.09
                if self.animation_loop >= 2:
                    self.animation_loop = 0
        if self.moving_right == True:
            self.moving_left = False
            if self.x_change == 0:
                self.image = right_animations[0]
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.09
                if self.animation_loop >= 2:
                    self.animation_loop = 0
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Life(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load('final/img/life.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Bomb(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.player = game.player
        self.spritesheet = Spritesheet('final/img/bomb.png')
        
        self.image = self.spritesheet.get_sprite(0, 0, 32, 32)
        self.rect.x, self.rect.y = self.player.rect.x, self.player.rect.y + 64

    def blitme(self):
        self.screen.blit(self.image, self.rect)