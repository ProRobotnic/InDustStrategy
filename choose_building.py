import pygame


class Board_of_building():
    def __init__(self, cell_size=24, quantity_of_cell=6, color=pygame.Color((0, 0, 0))):
        self.cell_size = cell_size
        self.quantity_of_cell = quantity_of_cell
        self.color = color

    def render(self, screen):
        for i in range(self.quantity_of_cell):
            for j in range(self.quantity_of_cell):
                pygame.draw.rect(screen, self.color, (i * self.cell_size + 750,
                                                               j * self.cell_size + 100, self.cell_size,
                                                               self.cell_size), 1)
