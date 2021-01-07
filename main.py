from config import *
from communications import *
from buildings import *
from menu import menu
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
menu.stage1(screen)
# --- end ---
pygame.quit()
