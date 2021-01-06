import sqlite3
import pprint
mas = [[[0, 1, 3, 0, 0],
        [0, 0, 3, 0, 0],
        [0, 3, 3, 0, 0],
        [0, 3, 0, 0, 0],
        [0, 3, 3, 0, 0]]]

players_coms = [{}, {}, {}, {}]
money = [100, 0, 0, 0]
turn = 0

# Подключение к БД
con = sqlite3.connect('buildings_db.sqlite')
# Создание курсора
cur = con.cursor()
# Выполнение запроса и получение всех результатов
buildings_db = cur.execute("""SELECT * FROM buildings""").fetchall()
print(buildings_db)

# Check of aviliability of communication in list (and creating it if doesn't avavliable)
def com_check(name, player):
    global players_coms
    global mas
    try:
        k = players_coms[player][name]
    except Exception:
        players_coms[player][name] = mas[player]


# Counting resourse cosuption of active buildings (connected to power)
def coms_consuption(name, com_id_list, player):
    global mas
    global players_coms
    if name == 'electricity'
    communications_check(name, mas[player], com_id_list, player)
    coms_map = players_coms[player][name]
    counter = 0
    for i in range(coms_map):
        for j in range(coms_map[i]):
            if coms_map[i][j] == '-1':
                pass




# Create/renew list of communication(i.e. electricity, heat and so on) map
def communications_check(name, com_id_list, player):
    global players_coms
    com_check(name, player)
    new_map = players_coms[player][name]  # New map of communications
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
    pprint.pprint(players_coms[player][name])
    players_coms[player][name][cord[0]][cord[1]] = -1
    p_c = players_coms[player][name]
    where = is_void_nearby(cord, p_c)
    print(where)
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


communications_check('electricity', [1, 2], 0)
pprint.pprint(players_coms)
print('Если не выдает ошибку - значит работает.')


# List 30х30 -> [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]