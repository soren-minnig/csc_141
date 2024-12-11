import pygame
from pygame.sprite import Group

from sprites import Life


class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (240, 240, 240)
        self.bg_color = (116, 181, 194)
        self.font = pygame.font.Font('final/fonts/Minecraft.ttf', 30)

        self.prep_images()

    def prep_images(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_lives()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score}"
        self.score_image = self.font.render(score_str, True,
                    self.text_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_lives(self):
        self.lives = Group()
        for life_number in range(self.stats.lives_left):
            life = Life(self.game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)