import pygame

class Alian():

    def __init__(self, screen):
        '''инициальзация пришельца'''
        self.screen = screen
        self.images = (pygame.image.load('pictures/alian.png'), pygame.image.load('pictures/alian_2.png'), pygame.image.load('pictures/alian_3.png'))
        self.image = self.images[2]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        '''отрисовка пришельца'''
        self.screen.blit(self.image, self.rect)