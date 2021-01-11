from config import *
from communications import buildings_db
import pygame


# Class for operating with buildings (place/delete)
class Building():
    image = None

    def __init__(self, image_path=''):
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


class PowerStation1(Building):
    def __init__(self, image_path):
        super(PowerStation1, self).__init__(image_path)


class PowerStation2(Building):
    def __init__(self, image_path):
        super(PowerStation2, self).__init__(image_path)


class Rocket1(Building):
    def __init__(self, image_path):
        super(Rocket1, self).__init__(image_path)

class Mortar(Building):
    def __init__(self, image_path):
        super(Mortar, self).__init__(image_path)

class ElectricHeater(Building):
    def __init__(self, image_path):
        super(ElectricHeater, self).__init__(image_path)

class EnergyGenerator1(Building):
    def __init__(self, image_path):
        super(EnergyGenerator1, self).__init__(image_path)




class MineStation(Building):
    def __init__(self, image_path):
        super(MineStation, self).__init__(image_path)


PowerSupply_1 = PowerStation1("resources/power_station.jpg")
PowerSupply_2 = PowerStation1("resources/power_station.jpg")
MiningStation = MineStation("resources/mine_station.jpg")
Rocket = Rocket1("resources/rocket.png")
Mortar = Mortar("resources/mortar.jpg")
EnergyGenerator1 = EnergyGenerator1("resources/gen.png")


buildings = [None, PowerSupply_1, PowerSupply_2, MiningStation, None, EnergyGenerator1, Rocket, Mortar]
