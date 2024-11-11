# UNFINISHED
import sys
from time import sleep
import pygame
from pygame.sprite import Sprite
import pygame.sprite


class Player:
    # Class to draw the player
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('12_a_ship_that_fires_bullets/img/sideways.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

     # Storing the player's horizontal position
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.movement()
        self.blitme()

        self.rect.y = self.y

    def movement(self):
        keys = pygame.key.get_pressed()
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

    def center_player(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)


class Rectangle(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.width, self.height = 32, 64
        self.color = (10, 10, 25)

        self.rect = pygame.Rect(1150, 600, self.width, self.height)

        self.y = float(self.rect.y)

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.y += 1
        self.rect.y = self.y

    def check_edges(self):
        return (self.rect.top == 0) or (self.rect.bottom == 800)
    
    def center_target(self):
        self.rect = pygame.Rect(1150, 600, self.width, self.height)
    

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.color = (84, 202, 232)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = game.player.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += 2.0
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Button:
    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (10, 10, 25)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    
class TargetPractice:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption('Target Practice')

        self.lives = 3
        self.counter = 0

        self.player = Player(self)
        self.target = pygame.sprite.Group()
        self.target.add(Rectangle(self))
        self.bullets = pygame.sprite.Group()

        self.start_button = Button(self, "Start")

        self.game_active = False

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.player.update()
                self.target.update()
                self._update_bullets()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_q]:
                sys.exit()
            if keys[pygame.K_SPACE]:
                self._fire_bullet()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_start_button(mouse_pos)

    def start(self):
        self.lives = 3
        self.counter = 0
        self.game_active = True

        self.bullets.empty()

        self.player.center_player()
        self.target.center_target()

        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        # Firing a bullet; if it exceed a certain limit,
        # new bullets cannot be fired
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # Removing bullets when they leave the screen
        for bullet in self.bullets.copy():
                if bullet.rect.left >= 1200:
                    self.bullets.remove(bullet)
                    if self.lives > 0:
                        self.lives -= 1
                        sleep(0.5)
                    else:
                        # Game over
                        self.game_active = False
                        pygame.mouse.set_visible(True)

        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.target, True, True)

    def _check_start_button(self, mouse_pos):
        if self.start_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.start()

    def _update_screen(self):
        self.screen.fill((255, 235, 235))
        self.player.blitme()
        for target in self.target:
            target.draw_target()
        if self.game_active:
            for bullet in self.bullets:
                bullet.draw_bullet()

        if not self.game_active:
            self.start_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    game = TargetPractice()
    game.run_game()