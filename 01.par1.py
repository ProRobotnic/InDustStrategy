import pygame

WIDTH = 800
FPS = 60
HEIGHT = 500

# --- class ----


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

    button1 = Button((340, 25), (120, 30), (0, 255, 0), "  Играть  ")
    button2 = Button((340, 75), (120, 30), (0, 255, 0), " Правила ")
    button3 = Button((340, 125), (120, 30), (0, 255, 0), "Настройки")
    button4 = Button((340, 175), (120, 30), (0, 255, 0), "  Выход  ")
    clock = pygame.time.Clock()
    running = True
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
                a = 1
            if button4.is_clicked(event):
                # exit
                pygame.quit()
                exit()
            if button2.is_clicked(event):
                a = 1
            if button3.is_clicked(event):
                a = 1

    # --- draws ---

        screen.fill((0, 250, 250))
        button1.draw(screen)
        button2.draw(screen)
        button4.draw(screen)
        button3.draw(screen)
        pygame.display.flip()

        # --- FPS ---

        clock.tick(FPS)


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
stage1(screen)

# --- end ---

pygame.quit()
