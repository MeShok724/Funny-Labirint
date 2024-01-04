import pygame
class Menu:

    buttons = []  # ['Первый этаж', 'Второй этаж', 'Третий этаж', 'Выход']
    number = 0
    backround = pygame.image.load("pictures/menu_background_2.png")

    def add(self, text, arial_50):
        self.buttons.append(arial_50.render(text, True, (255,255,0)))

    def change_number(self, set_upper):
        if set_upper and self.number != 0:

            self.number -= 1
        elif (not set_upper) and (self.number != (len(self.buttons) - 1)):
            self.number += 1

    def draw(self, screen, x, y, padding):
        i = 0
        background_rect = screen.get_rect()
        screen.blit(self.backround, background_rect)
        for option in self.buttons:
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * padding)
            if i == self.number:
                pygame.draw.rect(screen, (0, 100, 0), option_rect)
                # option[2] = (255, 255, 255)
            screen.blit(option, option_rect)
            i += 1