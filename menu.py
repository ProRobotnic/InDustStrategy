import pygame
from config import *
from events import screen_painter

menu_buttons = []
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


# --- class ----

# class Border(pygame.sprite.Sprite):


class Button(object):

    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0, 0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


def stage1(screen):
    global menu_buttons
    menu_screen = screen
    button1 = Button((516, 250), (120, 30), (255, 0, 0), "  Играть  ")
    button2 = Button((516, 300), (120, 30), (255, 0, 0), " Правила ")
    button3 = Button((516, 350), (120, 30), (255, 0, 0), "Настройки")
    button4 = Button((516, 400), (120, 30), (255, 0, 0), "  Выход  ")
    menu_buttons = [button1, button2, button3, button4]
    clock = pygame.time.Clock()
    running = True
    event_type = 'menu'
    while running:

        # --- events ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                event_type = 'board'
            if button4.is_clicked(event):
                pygame.quit()
                exit()
            if button2.is_clicked(event):
                a = 1
            if button3.is_clicked(event):
                a = 1

        # --- draws ---
        screen_painter(screen, event_type)
        pygame.display.flip()

        # --- FPS ---

        clock.tick(FPS)
