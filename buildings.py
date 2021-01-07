from config import *
from communications import buildings_db

# Class for operating with buildings (place/delete)
class Building():
    def __init__(self):
        self.void = 0

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
