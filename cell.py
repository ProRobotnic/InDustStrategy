import pygame


class Cell:
    # props:
    board = None
    is_selected = False
    building = None
    position_index = (0, 0)

    # calc props (readonly!)
    cell_top_left_x_y = (0, 0)

    def __init__(self, board, position_index, is_selected=False, building=None):
        self.position_index = position_index
        self.board = board
        self.is_selected = is_selected
        self.building = building

        self.cell_top_left_x_y = (
            board.position_top_left[0] +
            board.cell_size_px * self.position_index[0],
            board.position_top_left[1] + board.cell_size_px * self.position_index[1])

        self.render_building(self.building)

    def set_building(self, building):
        self.building = building
        self.render_building(self.building)

    def set_selected(self, is_selected):
        self.is_selected = is_selected
        self.set_background()

    def render_building(self, building):
        self.set_background()
        if building is None:
            image = pygame.image.load("resources/empty_cell.jpg")
        else:
            image = building.image

        # image resize
        img = pygame.transform.scale(
            image, (self.board.cell_size_px-2, self.board.cell_size_px-2))

        self.board.screen.blit(
            img, [self.cell_top_left_x_y[0], self.cell_top_left_x_y[1]])
        pygame.display.update()

    def set_background(self):
        background_color = pygame.Color("black")
        if self.is_selected:
            background_color = pygame.Color("red")
        pygame.draw.rect(self.board.screen,
                         background_color,
                         (
                             (self.cell_top_left_x_y[0],
                              self.cell_top_left_x_y[1]),
                             (self.board.cell_size_px, self.board.cell_size_px)
                         ), 2)
        pygame.display.flip()

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.building.image.get_rect().collidepoint(pygame.mouse.get_pos())
