import pygame
class Tablo:
    def __init__(self, screen, position_top_left, position_top_right):
        self.screen = screen
        self.position_top_left = position_top_left

        self.position_top_right = position_top_right
        self.quantity_of_money = quantity_of_money
        self.x1 = position_top_left[0]
        self.y1 = position_top_left[1]
        self.x2 = position_top_right[0]
        self.y2 = position_top_right[1]

    def render(self, screen, text):
        font = pygame.font.Font(None, 50)
        text = font.render(text, True, (100, 255, 100))
        pygame.draw.rect(screen, pygame.Color(255, 90, 0), ((1, 1), (5, 5), 1))
