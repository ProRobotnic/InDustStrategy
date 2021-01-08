import pygame


class Board:
    # создание поля
    def __init__(self, color=pygame.Color(70, 70, 70)):
        self.board = [[0] * 30 for _ in range(30)]
        # значения по умолчанию
        self.left = 1
        self.top = 1
        self.cell_size = 24
        self.color = color

    # настройка внешнего вида

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(30):
            for j in range(30):
                pygame.draw.rect(screen, self.color,
                                 (i * self.cell_size + 1, j * self.cell_size, self.cell_size, self.cell_size), 1)
