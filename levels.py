import Matrixes, alian, pygame
class Level():

    # floor = 1
    # matrix = Matrixes.matrix_1
    # start_row = 16
    # start_col = 10
    # alian_1_row = 6
    # alian_1_col = 12
    # alian_2_row = 2
    # alian_2_col = 9
    # door_row = 1
    # door_col = 10
    # wall_pic = pygame.image.load('pictures/wall_2.png')  # стена
    # floor_pic = pygame.image.load('pictures/floor.png')  # пол


    def __init__(self, screen):
        self.floor = 1
        self.matrix = Matrixes.matrix_1
        self.start_row = 15
        self.start_col = 10
        self.alian_1_row = 6
        self.alian_1_col = 12
        self.alian_2_row = 2
        self.alian_2_col = 9
        self.door_row = 1
        self.door_col = 10
        self.screen = screen
        self.wall_pic = pygame.image.load('pictures/wall_2.png')  # стена
        self.floor_pic = pygame.image.load('pictures/floor.png') # пол
        self.collizions = []

    def draw(self):
        cell_size = 50  # Размер каждой клетки в пикселях

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                x = col * cell_size  # Вычисляем координаты для отрисовки
                y = row * cell_size

                if self.matrix[row][col] == 1:
                    self.screen.blit(self.wall_pic, (x, y))
                else:
                    self.screen.blit(self.floor_pic, (x, y))

    def set_first(self):
        self.floor = 1
        self.matrix = Matrixes.matrix_1
        self.start_row = 15
        self.start_col = 10
        self.alian_1_row = 6
        self.alian_1_col = 12
        self.alian_2_row = 2
        self.alian_2_col = 9
        self.door_row = 1
        self.door_col = 10
        self.wall_pic = pygame.image.load('pictures/wall_2.png')  # стена
        self.floor_pic = pygame.image.load('pictures/floor.png')  # пол

    def set_second(self):
        self.floor = 2
        self.matrix = Matrixes.matrix_2
        self.start_row = 15
        self.start_col = 11
        self.alian_1_row = 5
        self.alian_1_col = 12
        self.alian_2_row = 2
        self.alian_2_col = 21
        self.door_row = 0
        self.door_col = 13
        self.wall_pic = pygame.image.load('pictures/wall_6.png')  # стена
        self.floor_pic = pygame.image.load('pictures/floor_4.png')  # пол

    def set_third(self):
        self.floor = 3
        self.matrix = Matrixes.matrix_3
        self.start_row = 15
        self.start_col = 10
        self.alian_1_row = 1
        self.alian_1_col = 15
        self.alian_2_row = 13
        self.alian_2_col = 16
        self.door_row = 5
        self.door_col = 23
        self.wall_pic = pygame.image.load('pictures/wall_3.png')  # стена
        self.floor_pic = pygame.image.load('pictures/floor_3.png')  # пол

    def set_collizions(self):
        cell_size = 50  # Размер каждой клетки в пикселях

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                x = col * cell_size  # Вычисляем координаты для отрисовки
                y = row * cell_size

                block = pygame.Rect(x, y, cell_size, cell_size)
                if self.matrix[row][col] == 1:
                    self.collizions.append((block, 'wall'))
                else:
                    self.collizions.append((block, 'floor'))