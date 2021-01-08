import os
import sys
from building import *
import pygame


class Board:

    # consts
    color = pygame.Color(0, 0, 0)
    cell_size_px = 24
    # screen

    # properties
    cell_count = (1, 1)  # cells count on board by x and y
    position_top_left = (0, 0)  # board position
    buildings = []

    # calculating props
    cells = [[]]  # cells on board

    def __init__(self, screen, cell_count, position_top_left, buildings=[]):
        self.screen = screen
        self.cell_count = cell_count
        self.position_top_left = position_top_left
        self.buildings = buildings

        self.cells = [[0] * self.cell_count[0]
                      for _ in range(self.cell_count[1])]

    def render(self):
        self.render_board()
        if len(self.buildings) > 0:
            self.render_building(self.buildings)

    def render_building(self, buildings):
        count = 0
        for i in range(len(self.cells[0])):
            for j in range(len(self.cells)):
                if len(buildings)-1 < count:
                    return

                # image resize
                img = pygame.transform.scale(
                    buildings[count].image, (self.cell_size_px-2, self.cell_size_px-2))

                top_left_x = self.position_top_left[0] + self.cell_size_px * i
                top_left_y = self.position_top_left[1] + self.cell_size_px * j
                self.screen.blit(img, [top_left_x, top_left_y])

                count += 1

    def render_board(self):
        for i in range(len(self.cells[0])):
            for j in range(len(self.cells)):
                top_left_x = self.position_top_left[0] + self.cell_size_px * i
                top_left_y = self.position_top_left[1] + self.cell_size_px * j

                pygame.draw.rect(
                    screen,
                    self.color,
                    (
                        (top_left_x, top_left_y),
                        (self.cell_size_px, self.cell_size_px)
                    ),
                    1)


# example - left board + building board
# uncomment for test
""" pygame.init()

buildings = []
station1 = PowerStation("resources/power_station.jpg")
station2 = MineStation("resources/mine_station.jpg")

buildings.append(station1)
buildings.append(station2)

size = 1000, 1000
screen = pygame.display.set_mode(size)
screen.fill((255, 0, 0))

board_pole = Board(screen, (6, 3), (100, 50))
board_buildings = Board(screen, (1, 4), (300, 50), buildings)


board_pole.render()
board_buildings.render()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit() """
