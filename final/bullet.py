import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = (227, 186, 75)

        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.midtop = game.player.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class EnemyBullet(Sprite):
    def __init__(self, game, midbottom):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = (57, 227, 193)
        self.midbottom = midbottom

        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.midbottom = self.midbottom

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)