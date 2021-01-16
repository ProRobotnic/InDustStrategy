from config import *
import menu
import pygame
from communications import *
from board import Board
import time

# -- Local variables --
attack_to = 0
event_type = 'menu'
pygame.init()
attack_was = 0
gl_screen = pygame.display.set_mode((WIDTH, HEIGHT))  # global screen to use in other files

# ----- Buttons and PlainText init -----
c_turn = turn
# init players boards
main_board = Board(gl_screen, 30, 30)
choosing_board = Board(gl_screen, 7, 1)
choosing_board.set_view(900, 150, 32)
choosing_board.choosing_table()

# menu buttons
menu_pic = menu.Picture((0, 0), (WIDTH, HEIGHT), "resources/MainMenuPhoto.png")
button1 = menu.Button((476, 250), (200, 35), (200, 30, 30), "  Играть  ")
button2 = menu.Button((476, 300), (0, 35), (200, 30, 30), " Правила ")
button3 = menu.Button((476, 350), (0, 35), (200, 30, 30), "Настройки")
button4 = menu.Button((476, 400), (200, 35), (200, 30, 30), "  Выход  ")
menu_buttons = [menu_pic, button1, button2, button3, button4]
# Common buttons
left_button = menu.Button((521, 262), (25, 25), (30, 30, 200), "<")
plus_minusPT = menu.PlainText((556, 262), (30, 25), (140, 140, 140), "0")
right_button = menu.Button((596, 262), (25, 25), (30, 30, 200), ">")
back_b = menu.Button((952, 690), (200, 30), (200, 30, 30), "Назад")
desc_pmPT = menu.PlainText((351, 220), (450, 30), (140, 140, 140), "Бомбим этого игрока:")
do_smthB = menu.Button((476, 300), (200, 30), (30, 30, 200), "В атаку!")
basic_choose_sc = [menu_pic, left_button, right_button, back_b, desc_pmPT, plus_minusPT, do_smthB]
# Next turn buttons
click_on_me_b = menu.Button((276, 312), (600, 100), (200, 30, 30), "Нажми на меня, чтобы начать следующий ход")
# Attack screen buttons
MortarsPT = menu.PlainText((750, 10), (300, 30), (135, 135, 135), "Количество атак: 0")
atck_sc = [MortarsPT, back_b]
# winscreen buttons
winB = menu.Button((451, 350), (250, 30), (200, 30, 30), "Вернуться в меню")
winPt = menu.PlainText((376, 250), (400, 60), (100, 15, 15), "Игрок n - победитель!")
# game screen buttons
next_turn_b = menu.Button((952, 690), (200, 30), (200, 30, 30), "Следующий ход")
attack_button = menu.Button((752, 690), (150, 30), (200, 30, 30), "Атаковать")
MoneyPT = menu.PlainText((750, 10), (115, 30), (30, 135, 30), "$:")
ElectricityPT = menu.PlainText((875, 10), (115, 30), (200, 200, 0), "E:")
HeatPT = menu.PlainText((1000, 10), (0, 30), (240, 30, 30), "H:")
board_objects = [ElectricityPT, HeatPT, MoneyPT, next_turn_b, attack_button]

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
                event_type = 'before game'
            if button4.is_clicked(event):
                pygame.quit()
                exit()
            if button2.is_clicked(event):
                a = 1
            if button3.is_clicked(event):
                a = 1
        # -- Events for game --
        elif event_type == 'before game':
            if left_button.is_clicked(event):
                players_amount -= 1
                if players_amount <= 1:
                    players_amount = 4
            if right_button.is_clicked(event):
                players_amount += 1
                if players_amount > 4:
                    players_amount = 2
            if back_b.is_clicked(event):
                event_type = 'menu'
            if do_smthB.is_clicked(event):
                event_type = 'board'
        elif event_type == 'board':
            if next_turn_b.is_clicked(event):
                event_type = 'nextturn'
            elif attack_button.is_clicked(event):
                event_type = 'attack'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_board.cell_clicked(event.pos, 'activate')
                choosing_board.cell_clicked(event.pos, 'activate')
                main_board.board = mas[turn]
                if choosing_board.active_cell != (-1, -1):
                    i, j = choosing_board.active_cell
                    if main_board.active_cell != (-1, -1) and buildings_db[choosing_board.board[j][i] - 1][2] <= money[
                        turn] and mas[turn][i][j] == 0:
                        if main_board.cell_clicked(event.pos) == 1:
                            y, x = main_board.active_cell
                            mas[turn][x][y] = choosing_board.board[j][i]
                            money[turn] -= buildings_db[choosing_board.board[j][i] - 1][2]
                            print(x, y)


        elif event_type == 'attack screen':
            if back_b.is_clicked(event):
                event_type = 'attack'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_board.cell_clicked(event.pos, 'activate')
                if attacks_count > 0 and main_board.active_cell != (-1, -1):
                    mas[attack_to][main_board.active_cell[1]][main_board.active_cell[0]] = 0
                    attack_was += 1
        elif event_type == 'nextturn':
            if click_on_me_b.is_clicked(event):
                turn += 1
                turn = turn % players_amount
                e_check = coms_consuption('electricity', electricity_list, turn)
                m_check = coms_consuption('money', electricity_list, turn)
                if e_check * -1 >= 0:
                    money[turn] += m_check * -1
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
            if do_smthB.is_clicked(event):
                event_type = 'attack screen'
            if back_b.is_clicked(event):
                event_type = 'board'
        elif event_type == 'win screen':
            if winB.is_clicked(event):
                event_type = 'menu'

    # --- draws ---

    if event_type == 'menu':
        gl_screen.fill((230, 230, 230))
        for button in menu_buttons:
            button.draw(gl_screen)

    elif event_type == 'attack screen':
        gl_screen.fill((245, 245, 245))
        main_board.render(mas[attack_to], False)
        for elem in atck_sc:
            elem.draw(gl_screen)
        attacks_count = count(7, turn) - attack_was
        MortarsPT.set_text("Количество атак: " + str(attacks_count))

    elif event_type == 'board':
        gl_screen.fill((245, 245, 245))
        MoneyPT.set_text("$: " + str(money[turn]), (230, 255, 230))
        h_check = coms_consuption('heat', heat_list, turn) * -1
        if h_check is None:
            h_check = 0
        HeatPT.set_text("H: " + str(h_check))
        e_check = coms_consuption('electricity', electricity_list, turn) * -1
        if e_check is None:
            e_check = 0
        ElectricityPT.set_text("E: " + str(e_check), (255, 255, 200))
        for elem in board_objects:
            elem.draw(gl_screen)
        main_board.render(mas[turn])
        choosing_board.render()


    elif event_type == 'before game':
        gl_screen.fill((245, 245, 245))
        for object in basic_choose_sc:
            object.draw(gl_screen)
        do_smthB.set_text("Подтвердть")
        desc_pmPT.set_text('Выберите количество игроков:')
        plus_minusPT.set_text(players_amount)

    elif event_type == 'nextturn':
        gl_screen.fill((245, 245, 245))
        click_on_me_b.draw(gl_screen)
        attack_was = 0

    elif event_type == 'attack':
        desc_pmPT.set_text('Бомбим этого игрока:')
        gl_screen.fill((245, 245, 245))
        if turn == attack_to:
            attack_to += 1
        attack_to %= players_amount
        plus_minusPT.set_text(str(attack_to + 1))
        do_smthB.set_text("В атаку!")
        for object in basic_choose_sc:
            object.draw(gl_screen)

    elif event_type == 'win screen':
        gl_screen.fill((245, 245, 245))
        winB.draw(gl_screen)
        winPt.set_text("Игрок " + str(turn + 1) + ' - победитель!')
        winPt.draw(gl_screen)
    for i in mas[turn]:
        for j in i:
            if j == win_condition:
                event_type = 'win screen'
                reset()
    pygame.display.flip()

    # --- FPS ---

    clock.tick(FPS)

# --- end ---
pygame.quit()

