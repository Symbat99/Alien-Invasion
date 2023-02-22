import pygame

image = pygame.image.load('images/alienship.png')
rect = image.get_rect()

screen = pygame.display.set_mode((1200,400))
screen_rect = screen.get_rect()

if rect.right >= screen_rect.right or rect.left <= 0:
