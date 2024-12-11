import pygame
import math
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, game, type):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.type = type
        self.name = 'final/img/enemyV1'

        if self.type == 1:
            self.name = 'final/img/enemyV1'
            self.multiplier = 1
        if self.type == 2:
            self.name = 'final/img/enemyV2'
            self.multiplier = 1.2

        self.image = pygame.image.load(self.name + '.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

        # Animation
        self.animation_loop = 0

        self.walking = True

    def update(self):
        if self.walking == True:
            self.animate()
            self.y += self.settings.enemy_speed * self.multiplier
            self.rect.y = self.y

    def animate(self):
        animations = [
            pygame.image.load(self.name + '.png'),
            pygame.image.load(self.name + '_2.png'),
            pygame.image.load(self.name + '.png'),
            pygame.image.load(self.name + '_3.png')
            ]
        
        self.image = animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.09 * self.multiplier
        if self.animation_loop >= 4:
            self.animation_loop = 0

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.top > screen_rect.bottom)
    

class BombEnemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.game = game
        self.settings = game.settings
        self.name = 'final/img/bomb'
        self.type = 3
        self.multiplier = 0.5

        self.image = pygame.image.load(self.name + '.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

        # Animation
        self.animation_loop = 0

        self.running = False
        self.exploding = False
        self.explode = False
        self.exploded = False
        self.timer = 0.5
        self.timer_explode = 0.5
        self.dt = game.clock.tick(60)/1000

    def update(self):
        if self.running == True:
            self.multiplier = 2.5

        if not self.exploding:
            self.animate()
            self.y += self.settings.enemy_speed * self.multiplier
            self.rect.y = self.y
        if self.exploding:
            pygame.mixer.Channel(2).play(self.game.explode_sound)
            self.image = pygame.image.load('final/img/bomb_4.png')
            self.timer -= self.dt
            if self.timer <= 0:
                self.image = pygame.image.load('final/img/bomb_ex.png')
                self.timer_explode -= self.dt
                if self.timer_explode <= 0:
                    self.kill()
            
    def animate(self):
        if self.running == True:
            self.name = 'final/img/bombR'

        animations = [
            pygame.image.load(self.name + '.png'),
            pygame.image.load(self.name + '_2.png'),
            pygame.image.load(self.name + '.png'),
            pygame.image.load(self.name + '_3.png')
            ]
        
        self.image = animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.09 * self.multiplier
        if self.animation_loop >= 4:
            self.animation_loop = 0

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.top > screen_rect.bottom)