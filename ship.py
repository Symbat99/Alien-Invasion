import pygame

class Ship:
    def __init__(self, ai_game):
        #get rectangle from screen
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # get screen rectangle
        self.screen_rect = ai_game.screen.get_rect()

        #load a ship image and get its rectangle
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        #set location of rectangle
        self.rect.midbottom = self.screen_rect.midbottom

        #координата центра коробля дробная
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        #перемещение коробля и проверка на границы экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #обновить координату которая управляет местоположением коробля
        self.rect.x = self.x

    def blitme(self):
        #draw ship
        self.screen.blit(self.image, self.rect)

