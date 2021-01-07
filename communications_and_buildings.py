import sqlite3
from copy import deepcopy
from pprint import pprint
class CommunicationTypeException(Exception):
    pass
mas = [[[1, 0, 3, 0, 3],
        [3, 0, 3, 0, 3],
        [3, 0, 3, 0, 3],
        [3, 0, 0, 0, 3],
        [3, 3, 3, 3, 3]]]

players_coms = [{}, {}, {}, {}]
money = [100, 0, 0, 0]
turn = 0

# Подключение к БД
con = sqlite3.connect('buildings_db.sqlite')
# Создание курсора
cur = con.cursor()
# Выполнение запроса и получение всех результатов
buildings_db = cur.execute("""SELECT * FROM buildings""").fetchall()
communications_db = cur.execute("""SELECT * FROM communications""").fetchall()


# Counting resourse cosuption of active buildings (connected to power)
def coms_consuption(name, com_id_list, player):
    global mas
    type_communication = 2
    for i in range(len(communications_db)):
        if name == communications_db[i][1]:
            type_communication += communications_db[i][0]
    if type_communication == 2:
        raise CommunicationTypeException
    else:
        communications_check(name, com_id_list, player)
        coms_map = players_coms[player][name]
        print(coms_map)
        counter = 0
        for i in range(len(coms_map)):
            for j in range(len(coms_map[i])):
                if coms_map[i][j] == -1:
                    com_consup = buildings_db[mas[player][i][j] - 1][type_communication]
                    print(com_consup)
                    if com_consup == None:
                        com_consup = 0
                    counter += com_consup
        return counter


# Standart copy() doesn't work on ^3 lists, so it's my_copy method
def my_copy(inp):
    out = []
    for i in range(len(inp)):
        out.append([])
        for k in range(len(inp[i])):
            out[i].append([])
            for j in range(len(inp[i][k])):
                out[i][k].append(inp[i][k][j])
    return out


# Create/renew list of communication(i.e. electricity, heat and so on) map
def communications_check(name, com_id_list, player):
    global players_coms
    global mas
    players_coms[player][name] = my_copy(mas)[player]
    new_map = players_coms[player][name][:]  # New map of communications
    for i in range(len(new_map)):
        for j in range(len(new_map[i])):
            if mas[player][i][j] in com_id_list:
                copy_cid = com_id_list.copy()
                copy_cid.append(-1)
                copy_cid.append(0)
                group_checker([i, j], name, copy_cid, player)
    players_coms[player][name] = new_map


# Find all groups, that connected to sourses of smth
def group_checker(cord, name, id_list, player):
    global players_coms
    players_coms[player][name][cord[0]][cord[1]] = -1
    p_c = players_coms[player][name]
    where = is_void_nearby(cord, p_c)
    if 1 in where:
        if p_c[cord[0] - 1][cord[1]] not in id_list:
            group_checker([cord[0] - 1, cord[1]], name, id_list, player)

    if 2 in where:
        if p_c[cord[0]][cord[1] + 1] not in id_list:
            group_checker([cord[0], cord[1] + 1], name, id_list, player)

    if 3 in where:
        if p_c[cord[0] + 1][cord[1]] not in id_list:
            group_checker([cord[0] + 1, cord[1]], name, id_list, player)

    if 4 in where:
        if p_c[cord[0]][cord[1] - 1] not in id_list:
            group_checker([cord[0], cord[1] - 1], name, id_list, player)


# List range check
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


## Class with methods for all buildings
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


print(coms_consuption('electricity', [1, 2], 0))
# pprint(players_coms)
print('Если не выдает ошибку - значит работает.')
pprint(mas)
# List 30х30 -> [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
