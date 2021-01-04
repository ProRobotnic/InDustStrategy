mas = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]
p1_coms = {}

coms_list = []
money = [100]
turn = 0


def coms_consuption(name, p_map, com_id_list):
    global coms_list
    communications_check(name, p_map, com_id_list)
    coms_map = p1_coms[name]
    for i in range(coms_map):
        for j in range(coms_map[i]):
            if e_map[i][j] != '-1':
                e_map[i][j] = 0
            else:
                e_map[i][j] = p_map[i][j]


# Create/renew list of communication(i.e. electricity, heat and so on) map
def communications_check(name, p_map, com_id_list):
    global p1_coms
    new_map = p_map.copy()  # New map of communications
    for i in range(new_map):
        for j in range(new_map[i]):
            if p_map[i][j] in com_id_list:
                group_checker(p_map[i][j], new_map, com_id_list.append[0])
            if new_map[i][j] != '-1':
                new_map[i][j] = 0
            else:
                new_map[i][j] = p_map[i][j]
    p1_coms[name] = new_map


# Find all groups, that connected to sourses of smth
def group_checker(cord, name, id_list):
    global coms_list
    where = is_void_nearby(cord)
    listtt[cord[0]][cord[1]] = -1
    if 1 in where and listtt[cord[0] - 1][cord[1]] not in id_list:
        group_checker([cord[0] - 1, cord[1]], listtt)
    if 2 in where and listtt[cord[0] - 1][cord[1]] not in id_list:
        group_checker([cord[0] - 1, cord[1]], listtt)
    if 3 in where and listtt[cord[0] + 1][cord[1] + 1] not in id_list:
        group_checker([cord[0] + 1, cord[1] + 1], listtt)
    if 4 in where and listtt[cord[0]][cord[1] - 1] not in id_list:
        group_checker([cord[0], cord[1] + 1], listtt)


def is_void_nearby(cord, listt):
    sides = []
    # Sides are:  ->
    #    //      1     \\
    #  4 <current  square> 2
    #    \\      3     //
    if cord[0] >= 1 and cord:
        sides.append(1)
    if cord[1] < len(listt[cord[0]]) - 1:
        sides.append(2)
    if cord[0] < len(listt) - 1:
        sides.append(3)
    if cord[1] >= 1:
        sides.append(4)
    return sides


## Parent-class for all buildings
class Building():
    def __init__(self):
        self.id = 0
        self.cost = 10
        self.power_consuption = 0  # Resourse consuption;
        self.heat_consuption = 0  # If < 0, then resourses
        self.money_consuption = 0  # are generated.

    def place(self, cord):
        global mas
        global money
        global turn
        if mas[cord[0]][cord[1]] == 0 and self.cost <= money[turn]:
            mas[cord[0]][cord[1]] = self.id
            money[turn] -= self.cost
        else:
            print('no')

    def destroy(self, cord):
        global mas
        mas[cord[0], cord[1]] = self.void


class PowerSupply_1(Building):
    def __init__(self):
        self.id = 1
        self.cost = 5


class PowerSupply_2(Building):
    def __init__(self):
        self.id = 2
        self.cost = 15


class MiningStation_1(Building):
    def __init__(self):
        self.id = 3
        self.cost = 10
        self.energy_consuption = 20


class Furnace(Building):
    def __init__(self):
        self.id = 4
        self.cost = 5
        self.heat_consuption = 10


class ElectricHeater(Building):
    def __init__(self):
        self.id = 5
        self.cost = 10
        self.energy_consuption = 30
        self.heat_consuption = -50


class EnergyGenerator_1(Building):
    def __init__(self):
        self.id = 5
        self.cost = 10
        self.energy_consuption = -50
        self.heat_consuption = 25


class EnergyGenerator_2(Building):
    def __init__(self):
        self.id = 6
        self.cost = 25
        self.energy_consuption = -125
        self.heat_consuption = 50

print('Если не выдает ошибку - значит работает.')
