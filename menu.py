import pygame
from config import *

menu_buttons = []
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


# --- class ----

# class Border(pygame.sprite.Sprite):





class PlainText(object):
    def __init__(self, position, size, color, text):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.color = color
        self.rect = pygame.Rect((0, 0), size)
        self.pos = position
        self.size = size

        self.font = pygame.font.SysFont('None', 32)
        text = self.font.render(text, True, (255, 200, 200))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)
        self.rect.topleft = position

    def set_text(self, new_text, font_color=(255, 200, 200)):
        new_text = str(new_text)
        self.image.fill(self.color)
        self.rect = pygame.Rect((0, 0), self.size)
        text = self.font.render(new_text, True, font_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        self.image.blit(text, text_rect)
        self.rect.topleft = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Button(PlainText):
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)
