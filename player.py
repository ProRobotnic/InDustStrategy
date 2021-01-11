from board import Board

class Player:
    is_active = False
    board_main = None # left board
    board_buildings = None  # board for buildings

    building_places = None 

    def __init__(self, screen, buildings):
        board_main = Board(screen, (30,30), (0,0))
        board_buildings = Board(screen, (3,1), (750,75), buildings)

        board_main.render()
        board_buildings.render()

    def set_actice(is_active):
        self.is_active = is_active

    def display_update(self, buidingIds)
