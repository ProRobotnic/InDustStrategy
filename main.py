from buildings import *
import menu
import pygame

pygame.init()

gl_screen = pygame.display.set_mode((WIDTH, HEIGHT)) # global screen to use in other files
menu.stage1(gl_screen)

# --- end ---
pygame.quit()
