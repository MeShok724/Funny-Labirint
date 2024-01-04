import pygame, Matrixes


spaun_x = 50 * 10 + 9
spaun_y = 50 * 16 - 3

class Character():

    def __init__(self, screen):
        '''инициальзация человека'''
        self.screen = screen

        self.images = (pygame.image.load('pictures/anim_1.png'), pygame.image.load('pictures/anim_2.png'), pygame.image.load('pictures/anim_3.png'),
                       pygame.image.load('pictures/anim_4.png'), pygame.image.load('pictures/anim_5.png'), pygame.image.load('pictures/anim_6.png'),
                       pygame.image.load('pictures/anim_7.png'), pygame.image.load('pictures/anim_8.png'), pygame.image.load('pictures/anim_9.png'),
                       pygame.image.load('pictures/anim_10.png'), pygame.image.load('pictures/anim_11.png'), pygame.image.load('pictures/anim_12.png'))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = spaun_x
        self.rect.bottom = spaun_y
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        '''отрисовка человека'''
        self.screen.blit(self.image, self.rect)

    def update(self, collizions):
        # обновление положения человека
        if self.mright and self.rect.right < self.screen_rect.right:
            self.image = self.images[9]
            self.rect.centerx += 1
            for block in collizions:
                if block[1] == 'wall':
                    block_rect = block[0]
                    if self.rect.colliderect(block_rect):
                        self.rect.right = block_rect.left


        if self.mleft and self.rect.left > self.screen_rect.left:
            self.image = self.images[6]
            self.rect.centerx -= 1
            for block in collizions:
                if block[1] == 'wall':
                    block_rect = block[0]
                    if self.rect.colliderect(block_rect):
                        self.rect.left = block_rect.right

        if self.mup and self.rect.top > self.screen_rect.top:
            self.image = self.images[4]
            self.rect.centery -= 1
            for block in collizions:
                if block[1] == 'wall':
                    block_rect = block[0]
                    if self.rect.colliderect(block_rect):
                        self.rect.top = block_rect.bottom

        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.image = self.images[1]
            self.rect.centery += 1
            for block in collizions:
                if block[1] == 'wall':
                    block_rect = block[0]
                    if self.rect.colliderect(block_rect):
                        self.rect.bottom = block_rect.top