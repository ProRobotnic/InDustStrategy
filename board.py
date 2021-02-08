import os
import sys
import pygame
from communications import my_copy, buildings_db
import pygame

class Board:
    # создание поля
    def __init__(self, screen, width, height, cell_color=(100, 100, 100)):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = [[0] * width for _ in range(height)]
        self.left = 1
        self.top = 1
        self.cell_size = 24
        self.click = (0, 0)
        self.active_cell = (-1, -1)
        self.active_color = 'red'
        self.cell_color = cell_color
        self.can_be_deleted_from = True

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def cell_clicked(self, cord, activate_or_deactivate='activate'):
        if activate_or_deactivate == 'activate':
            x_c, y_c = cord
            cs = self.cell_size
            t = self.top
            l = self.left
            for y in range(self.height):
                for x in range(self.width):
                    if (l + cs * x <= x_c and x_c < l + cs * x + cs) and (
                            t + cs * y <= y_c and y_c < t + cs * y + cs):
                        self.active_cell = (x, y)
                        return (True)
        elif activate_or_deactivate == 'deactivate':
            self.active_cell = (-1, -1)

    def render(self, pole=[], buildings_visible=True):
        if pole != []:
            self.board = pole
        self.out = None
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.screen, self.cell_color, (
                    (self.left + self.cell_size * x, self.top + self.cell_size * y), (self.cell_size, self.cell_size)),
                                 1)
                if self.board[y][x] != 0 and buildings_visible:
                    try:
                        try:
                            image = pygame.image.load("buildings/" + str(self.board[y][x]) + ".jpg")
                        except Exception:
                            image = pygame.image.load("buildings/" + str(self.board[y][x]) + ".png")
                        img = pygame.transform.scale(
                            image, (self.cell_size - 2, self.cell_size - 2))
                        self.screen.blit(
                            img,
                            (self.left + self.cell_size * x + 1, self.top + self.cell_size * y + 1))
                    except Exception:
                        try:
                            image = pygame.image.load("buildings/default.jpg")
                            img = pygame.transform.scale(
                                image, (self.cell_size - 2, self.cell_size - 2))
                            self.screen.blit(
                                img,
                                (self.left + self.cell_size * x + 1, self.top + self.cell_size * y + 1))
                        except Exception:
                            pass
        if self.active_cell != (-1, -1):
            x, y = self.active_cell
            pygame.draw.rect(self.screen, self.active_color, (
                (self.left + self.cell_size * x, self.top + self.cell_size * y), (self.cell_size, self.cell_size)), 1)


    def choosing_table(self):
        builds = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    row.append(buildings_db[i * self.width + j][0])
                except Exception:
                    row.append(0)
            builds.append(row)
        self.board = builds
        self.can_be_deleted_from = False