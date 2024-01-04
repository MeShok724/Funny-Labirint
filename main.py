import pygame
import time
import sys, os
import controls
from levels import Level
from Character import Character
from alian import Alian
from menu import Menu


def run():

    # настройка fps
    clock = pygame.time.Clock()
    fps = 200

    # загрузка изображений
    im_win = pygame.image.load('pictures/you_win.png')
    im_lose = pygame.image.load('pictures/you_lose.png')

    # инициализация pygame
    pygame.init()

    # стартовое меню экран
    screen_start = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Корабль пришельцев')
    bg_color_start = (255, 255, 255)

    # стартовое меню пункты
    arial_50 = pygame.font.SysFont('arial', 50)
    menu = Menu
    menu.add(menu, 'Первый этаж', arial_50)
    menu.add(menu, 'Второй этаж', arial_50)
    menu.add(menu, 'Третий этаж', arial_50)
    menu.add(menu, 'Выход', arial_50)

    # цикл меню
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    sys.exit()
                if e.key == pygame.K_w:
                    menu.change_number(menu, True)
                if e.key == pygame.K_s:
                    menu.change_number(menu, False)
                if e.key == pygame.K_SPACE:
                    if menu.number == 3:
                        sys.exit()
                    running = False

        # отрисовка меню
        screen_start.fill(bg_color_start)
        menu.draw(menu, screen_start, 150, 70, 70)
        pygame.display.flip()

    # игровой экран
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Корабль пришельцев')
    bg_color = (0, 0, 0)

    # инициализация уровня
    level = Level(screen)

    if menu.number == 0:
        level.set_first()
    elif menu.number == 1:
        level.set_second()
    elif menu.number == 2:
        level.set_third()

    # инициализация игровых персонажей и стенок
    level.set_collizions()
    character = Character(screen)
    character.rect.top = 50 * level.start_row
    character.rect.left = 50 * level.start_col
    alian_1, alian_2 = Alian(screen), Alian(screen)
    # alian_1.image = alian_2.images[0]
    alian_1.rect.top = 50 * level.alian_1_row
    alian_1.rect.left = 50 * level.alian_1_col
    alian_2.rect.top = 50 * level.alian_2_row
    alian_2.rect.left = 50 * level.alian_2_col

    # Бесконечный цикл с игрой
    while True:
        controls.events(character)
        character.update(level.collizions)
        level.draw()
        controls.update(level, bg_color, screen, alian_1, alian_2, character)

        clock.tick(fps)

        row, col = character.rect.centery // 50, character.rect.centerx // 50
        if row == level.door_row and col == level.door_col:
            break
        if (row == level.alian_1_row and col == level.alian_1_col) or (row == level.alian_2_row and col ==
                    level.alian_2_col):
            character.rect.top = 50 * level.start_row
            character.rect.left = 50 * level.start_col
            screen.blit(im_lose, (0, 0))
            pygame.display.flip()
            time.sleep(2)

    # завершение игры
    screen.blit(im_win, (0,0))
    pygame.display.flip()
    time.sleep(2)


# Начало основной программы
run()

