from config import *
from communications import buildings_db
import pygame

# Class for operating with buildings (place/delete)
class Building():
    image = None

    def __init__(self, image_path = ''):
        self.void = 0
            
        if len(image_path) > 0:
            self.image = pygame.image.load(image_path)

    def place(self, id, cord, player):
        global mas
        global money
        if mas[player][cord[0]][cord[1]] == 0 and buildings_db[id][2] <= money[player]:
            mas[player][cord[0]][cord[1]] = id
            money[player] -= buildings_db[id][2]
        else:
            print('Not enough money')
            # Need-to-update in future

    def destroy(self, cord, player):
        global mas
        mas[player][cord[0]][cord[1]] = self.void

class PowerStation(Building):
    def __init__(self, image_path):
        super(PowerStation, self).__init__(image_path)

class MineStation(Building):
    def __init__(self, image_path):
        super(MineStation, self).__init__(image_path)

