from config import *
from buildings import *
import menu
import pygame
from feature_board import Board
import time

game_board = Board()
# -- Local variables --
attack_to = 0
event_type = 'attack'
pygame.init()
# -- Buttons --
gl_screen = pygame.display.set_mode((WIDTH, HEIGHT))  # global screen to use in other files
left_button = menu.Button((486, 262), (25, 25), (30, 30, 200), "<")
right_button = menu.Button((561, 262), (25, 25), (30, 30, 200), ">")
conf_attack = menu.Button((391, 300), (300, 30), (30, 30, 200), "Выбрать игрока для атаки")
back_attack = menu.Button((952, 690), (200, 30), (200, 30, 30), "Назад")
attack_button = menu.Button((752, 690), (150, 30), (200, 30, 30), "Атаковать")
click_on_me_b = menu.Button((276, 312), (600, 100), (200, 30, 30), "Нажми на меня, чтобы начать следующий ход")
next_turn_b = menu.Button((952, 690), (200, 30), (200, 30, 30), "Следующий ход")
button1 = menu.Button((476, 250), (200, 35), (200, 30, 30), "  Играть  ")
button2 = menu.Button((476, 300), (200, 35), (200, 30, 30), " Правила ")
button3 = menu.Button((476, 350), (200, 35), (200, 30, 30), "Настройки")
button4 = menu.Button((476, 400), (200, 35), (200, 30, 30), "  Выход  ")
menu_buttons = [button1, button2, button3, button4]
# -- Main game cycle --
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
            if attack_button.is_clicked(event):
                event_type = 'attack'
        elif event_type == 'nextturn':
            if click_on_me_b.is_clicked(event):
                global turn
                turn += 1
                turn = turn % players_amount
                event_type = 'board'
        elif event_type == 'attack':
            if left_button.is_clicked(event):
                attack_to -= 1
                if turn == attack_to:
                    attack_to -= 1
                if attack_to < 0:
                    attack_to = players_amount - attack_to
            if right_button.is_clicked(event):
                attack_to += 1
                if turn == attack_to:
                    attack_to += 1
                if attack_to > players_amount:
                    attack_to %= players_amount
            if conf_attack.is_clicked(event):
                print('conf_attack is clicked.')
                pass
            if back_attack.is_clicked(event):
                event_type = 'board'

    # --- draws ---

    if event_type == 'menu':
        gl_screen.fill((230, 230, 230))
        for button in menu_buttons:
            button.draw(gl_screen)

    elif event_type == 'board':
        gl_screen.fill((245, 245, 245))
        next_turn_b.draw(gl_screen)
        game_board.render(gl_screen)
        attack_button.draw(gl_screen)

    elif event_type == 'nextturn':
        gl_screen.fill((245, 245, 245))
        click_on_me_b.draw(gl_screen)
    elif event_type == 'attack':
        gl_screen.fill((245, 245, 245))
        left_button.draw(gl_screen)
        conf_attack.draw(gl_screen)
        right_button.draw(gl_screen)
        if turn == attack_to:
            attack_to += 1
        attack_to %= players_amount
        font = pygame.font.Font(None, 50)
        text = font.render(str(attack_to), True, (30, 30, 150))
        gl_screen.blit(text, (526, 262))
        back_attack.draw(gl_screen)

    pygame.display.flip()

    # --- FPS ---

    clock.tick(FPS)

# --- end ---
pygame.quit()
