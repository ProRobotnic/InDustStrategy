import os
import sys
from building import *
import pygame
from cell import *
from communications import my_copy


class Board:
    # consts
    color = pygame.Color(0, 0, 0)
    cell_size_px = 24
    screen = None

    # properties
    cell_count = (1, 1)  # cells count on board by x and y
    cell_selected = None
    position_top_left = (0, 0)  # board position
    buildings = []

    # calculating props
    cells = None  # cells on board

    def __init__(self, screen, cell_count, position_top_left, buildings=[]):
        self.screen = screen
        self.cell_count = cell_count
        self.position_top_left = position_top_left
        self.buildings = buildings

    def render_from_mas(self, turn):
        builds = mas[turn]
        for i in range(len(builds)):
            for j in range(len(builds[i])):
                print(builds[i][j])
                self.cells[j][i].set_building(buildings[builds[i][j]])

    def render(self):
        count = 0
        self.cells = []
        for i in range(self.cell_count[0]):
            row = []
            for j in range(self.cell_count[1]):
                building = None
                if len(self.buildings) - 1 > count:
                    building = self.buildings[count]
                cell = Cell(self, (i, j), False, building)
                row.append(cell)
                count += 1
            self.cells.append(row)

    def get_cell_index(self, coordinate_x_y):
        if self.position_top_left[0] <= coordinate_x_y[0] <= self.position_top_left[0] + self.cell_size_px * \
                self.cell_count[0]:
            if self.position_top_left[1] <= coordinate_x_y[1] <= self.position_top_left[1] + self.cell_size_px * \
                    self.cell_count[1]:
                x = coordinate_x_y[0] - self.position_top_left[0]
                y = coordinate_x_y[1] - self.position_top_left[1]
                return (x // self.cell_size_px, y // self.cell_size_px)
            else:
                return None
        else:
            return None

    def get_cell(self, coordinate_x_y):
        index = self.get_cell_index(coordinate_x_y)
        if index is None:
            return None
        try:
            return self.cells[index[0]][index[1]]
        except Exception:
            return None

    def get_mouse_click(self, coordinate_x_y):
        cell = self.get_cell(coordinate_x_y)
        if cell is not None:
            if self.cell_selected is not None:
                self.cell_selected.set_selected(False)

            self.cell_selected = cell
            self.cell_selected.set_selected(True)


