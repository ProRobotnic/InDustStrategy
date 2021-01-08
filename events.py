import pygame
from config import *
import time
from feature_board import Board

#Def to draw on pygame screen
def screen_painter(screen, event_type):
    if event_type == 'menu':
        screen.fill((230, 230, 230))
        for button in menu.menu_buttons:
            button.draw(screen)
    elif event_type == 'board':
        screen.fill((245, 245, 245))
        game_board = Board()
        game_board.render(screen)

    elif event_type == 'nextturn':
        global turn
        screen.fill((245, 245, 245))
        time.sleep(time_to_next_turn)
        turn += 1
        screen_painter(screen, 'board')

