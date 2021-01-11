import os
import sys
from building import *
import pygame
from cell import *


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
        if self.position_top_left[0] <= coordinate_x_y[0] <= self.position_top_left[0] + self.cell_size_px * self.cell_count[0]:
            if self.position_top_left[1] <= coordinate_x_y[1] <= self.position_top_left[1] + self.cell_size_px * self.cell_count[1]:
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
        return self.cells[index[0]][index[1]]

    def get_mouse_click(self, coordinate_x_y):
        cell = self.get_cell(event.pos)
        if cell is not None:
            if self.cell_selected is not None:
                self.cell_selected.set_selected(False)

            self.cell_selected = cell
            self.cell_selected.set_selected(True)


# example - left board + building board
# uncomment for test
'''
pygame.init()

buildings = []
station1 = PowerStation("resources/power_station.jpg")
station2 = MineStation("resources/mine_station.jpg")

buildings.append(station1)
buildings.append(station2)

size = 1152, 720
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

board_main = Board(screen, (30, 30), (0, 0))
board_buildings = Board(screen, (2, 2), (900, 150), buildings)

board_main.render()

board_main.cells[5][1].set_building(station1)
board_main.cells[6][6].set_building(station2)

board_buildings.render()


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            board_buildings.get_mouse_click(event.pos)
            board_main.get_mouse_click(event.pos)

            # copy building to main board if building not empty
            # todo: add money/energy logic!
            if board_main.cell_selected is not None and \
                board_main.cell_selected.building is None and \
                board_buildings.cell_selected is not None and \
                board_buildings.cell_selected.building is not None:
                    board_main.cell_selected.set_building(board_buildings.cell_selected.building)

pygame.quit()
'''
