import pygame

class DifficultyButton:
    def __init__(self, game, x, y, color, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.x, self.y = x, y
        self.width, self.height = 200, 50
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('final/fonts/Minecraft.ttf', 30)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)