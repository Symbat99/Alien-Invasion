import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # get rectangle from screen
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien spaceship image and get its rectangle
        self.image = pygame.image.load('images/alienship.png')
        self.rect = self.image.get_rect()

        # set location of rectangle
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # координата центра коробля дробная
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect() #размер экрана
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: #если top_right достигает края экрана и если top_left достигает 0
            return True

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
