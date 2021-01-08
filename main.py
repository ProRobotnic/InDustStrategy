from config import *
from buildings import *
import menu
import pygame
from feature_board import Board
from events import screen_painter

pygame.init()

gl_screen = pygame.display.set_mode((WIDTH, HEIGHT))  # global screen to use in other files
next_turn_b = menu.Button((1052, 760), (180, 30), (255, 0, 0), "Следующий ход")
button1 = menu.Button((476, 250), (200, 35), (255, 0, 0), "  Играть  ")
button2 = menu.Button((476, 300), (200, 35), (255, 0, 0), " Правила ")
button3 = menu.Button((476, 350), (200, 35), (255, 0, 0), "Настройки")
button4 = menu.Button((476, 400), (200, 35), (255, 0, 0), "  Выход  ")
menu_buttons = [button1, button2, button3, button4]
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
        # -- Events for menu --
        if event_type == 'menu':
            if button1.is_clicked(event):
                event_type = 'board'
            if button4.is_clicked(event):
                pygame.quit()
                exit()
            if button2.is_clicked(event):
                a = 1
            if button3.is_clicked(event):
                a = 1
        # -- Events for game --
        elif event_type == 'board':
            if next_turn_b.is_clicked(event):
                event_type = 'nextturn'

    # --- draws ---
    screen_painter(gl_screen, event_type)
    pygame.display.flip()

    # --- FPS ---

    clock.tick(FPS)

# --- end ---
pygame.quit()
