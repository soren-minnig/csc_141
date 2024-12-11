import pygame


class Background:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('final/img/map.png')
        self.rect = self.image.get_rect()
        
    # def update(self):
    #     self.rect_copy.y += 2
    #     self.rect_copy2.y += 2

    #     if self.rect_copy.bottom <= 0:
    #         self.rect_copy.bottom = self.rect_copy2.top
    #     if self.rect_copy.bottom <= 0:
    #         self.rect_copy2.bottom = self.rect_copy.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)