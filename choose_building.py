import pygame
size = 1152, 720
screen = pygame.display.set_mode(size)


class Board_of_building():
    def __init__(self, cell_size, quantity_of_cell, color):
        self.cell_size = cell_size
        self.quantity_of_cell = quantity_of_cell
        self.color = color

    def render(self):
        for i in range(self.quantity_of_cell):
            for j in range(self.quantity_of_cell):
                pygame.draw.rect(screen, pygame.Color("red"), (i * self.cell_size + 750,
                                                               j * self.cell_size + 100, self.cell_size, self.cell_size), 1)
