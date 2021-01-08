import pygame
size = 1152, 720
screen = pygame.display.set_mode(size)


class Board:
    # создание поля
    left = 1
    top = 1
    cell_size = 24
    color = (1,1,1) # rgb
    board_size = 30

    def __init__(self):
        self.board = [[0] * 30 for _ in range(30)]
        # значения по умолчанию
        self.left = 1
        self.top = 1
        self.cell_size = 24

    # настройка внешнего вида

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, sc):
        for i in range(board_size):
            for j in range(board_size):
                pygame.draw.rect(screen, pygame.Color(
                    255, 255, 255), (i * self.cell_size + 1, j * self.cell_size + 1, self.cell_size, self.cell_size), 1)
board = Board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()