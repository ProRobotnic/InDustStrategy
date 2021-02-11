import pygame
from config import *

menu_buttons = []
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


# --- class ----

# class Border(pygame.sprite.Sprite):
class Picture(object):
    def __init__(self, position, size, path):
        self.pos = position
        self.size = size
        image = pygame.image.load(str(path))
        self.image = pygame.transform.scale(
            image, (self.size[0], self.size[1]))

    def draw(self, screen):
        x, y = self.pos
        screen.blit(self.image, (x, y))

    def move(self, x1, y1):
        x, y = self.pos
        self.pos = (x + x1, y + y1)

    def change_pic(self, path):
        image = pygame.image.load(str(path))
        self.image = pygame.transform.scale(
            image, (self.size[0], self.size[1]))

class PicturePlainText(Picture):
    def __init__(self, position, size, text, path=None, font_color='white'):
        self.size = size
        self.pos = position
        image = pygame.image.load(str(path))
        self.image = pygame.transform.scale(
            image, (self.size[0], self.size[1]))
        self.rect = pygame.Rect((0, 0), size)
        self.path = path
        if path is not None:

            self.font = pygame.font.SysFont('None', 32)
            text = self.font.render(text, True, font_color)
            text_rect = text.get_rect()
            text_rect.center = self.rect.center

            self.image.blit(text, text_rect)
        self.rect.topleft = position

    def set_text(self, new_text, font_color='white'):
        if self.path is not None:
            image = pygame.image.load(str(self.path))
            self.image = pygame.transform.scale(
            image, (self.size[0], self.size[1]))
            self.rect = pygame.Rect((0, 0), self.size)
            text = self.font.render(new_text, True, font_color)
            text_rect = text.get_rect()
            text_rect.center = self.rect.center

            self.image.blit(text, text_rect)
            self.rect.topleft = self.pos


class PictureButton(PicturePlainText):
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


class PlainText(object):
    def __init__(self, position, size, color, text, font_size=32):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.color = color
        self.rect = pygame.Rect((0, 0), size)
        self.pos = position
        self.size = size
        self.font_size = font_size

        self.font = pygame.font.SysFont('None', self.font_size)
        text = self.font.render(text, True, 'white')
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)
        self.rect.topleft = position

    def set_text(self, new_text, font_color='white'):
        new_text = str(new_text)
        self.image.fill(self.color)
        self.rect = pygame.Rect((0, 0), self.size)
        text = self.font.render(new_text, True, font_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        self.image.blit(text, text_rect)
        self.rect.topleft = self.pos

    def draw(self, screen):
        self.rect.topleft = self.pos
        screen.blit(self.image, self.rect)

    def move(self, x1, y1):
        x, y = self.pos
        self.pos = (x + x1, y + y1)


class Button(PlainText):
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

