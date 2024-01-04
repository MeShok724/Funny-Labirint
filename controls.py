import pygame, sys, Matrixes
from Character import Character


def events(character):

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.KEYDOWN:

            # обработка нажатия клавиши
            if event.key == pygame.K_d:
                character.mright = True
            elif event.key == pygame.K_a:
                character.mleft = True
            elif event.key == pygame.K_w:
                character.mup = True
            elif event.key == pygame.K_s:
                character.mdown = True

        if event.type == pygame.KEYUP:

            # обработка отжатия клавиши
            if event.key == pygame.K_d:
                character.mright = False
                character.image = character.images[10]
            elif event.key == pygame.K_a:
                character.mleft = False
                character.image = character.images[7]
            elif event.key == pygame.K_w:
                character.image = character.images[3]
                character.mup = False
            elif event.key == pygame.K_s:
                character.image = character.images[0]
                character.mdown = False


def update(level, bg_color, screen, alian_1, alian_2, character):

    # screen.fill(bg_color)
    alian_1.output()
    alian_2.output()
    character.output()
    screen.blit(pygame.image.load('pictures/door.png'), (level.door_col * 50, level.door_row * 50))
    pygame.display.flip()