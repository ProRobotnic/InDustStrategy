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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.click(cell)


# example - left board + building board
# uncomment for test
"""pygame.init()

buildings = []
station1 = PowerStation("resources/power_station.jpg")
station2 = MineStation("resources/mine_station.jpg")

buildings.append(station1)
buildings.append(station2)
size = 1152, 720
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
board_pole = Board(screen, (30, 30), (0, 0))
board_buildings = Board(screen, (2, 2), (900, 150), buildings)


board_pole.render()

board_pole.cells[5][1].set_building(station1)
board_pole.cells[6][6].set_building(station2)

board_buildings.render()


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #board_pole.get_click(event.pos, )
            #board_pole.cells[2][1].set_building(None)
            x,y = event.pos
            for i in range(board_pole.cell_count[0]):
                for j in range(board_pole.cell_count[1]):
                    c = board_pole.cells[i][j]
                    
                    if c.building is not None and c.building.image.get_rect().collidepoint(event.pos): 
                        b = c.is_clicked()
                        board_pole.cells[i][j].set_building(None)

pygame.quit()"""
