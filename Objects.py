import pygame
from config import *
import os
import time
from communications import *

def load_image(name, colorkey=None):
    # Загрузка изображения
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return '0'
    image = pygame.image.load(fullname)
    return image

def sign(num):
    return -1 if num < 0 else 1


class GroupMoving:
    def __init__(self, sprite_group, start_pos, end_pos, speed):
        self.sprites = sprite_group
        self.pos = start_pos
        self.get_to = end_pos
        self.moving = False
        self.speed = speed
        self.next_sprites = sprite_group
        self.amount = 1
        self.current_position = 0

    def move(self, amount=1, sprite_group=None):
        if not self.moving:
            if sprite_group is not None and amount == 1:
                print('here')
                self.sprites = sprite_group
            elif sprite_group is not None and amount == 2:
                self.next_sprites = sprite_group
            self.moving = True
            self.amount = amount
            self.dest = (sign(self.pos[0] - self.get_to[0]) * -1,
                     sign(self.pos[1] - self.get_to[1]) * -1)
            self.dist = [(self.pos[0] - self.get_to[0]) * -1, (self.pos[1] - self.get_to[1]) * -1]
        else:
            if sprite_group is not None and amount == 1:
                self.sprites = sprite_group
            elif sprite_group is not None and amount == 2:
                self.next_sprites = sprite_group
            self.dest = (self.dest[0] * -1, self.dest[1] * -1)
            self.dist = [(((self.pos[0] - self.get_to[0]) * -1) - self.dist[0]) * -1,
                         (((self.pos[1] - self.get_to[1]) * -1) - self.dist[1]) * -1]
            self.pos, self.get_to = self.get_to, self.pos
    def set_sprite_group(self, sprites, current=True):
        if current:
            self.sprites = sprites
        else:
            self.next_sprites = sprites

    def update(self, screen):
        if self.moving:
            for elem in self.sprites:
                if (self.dist[0] - self.speed * self.dest[0]) * self.dist[0] > 0:
                    x_move = self.speed * self.dest[0]
                elif (self.dist[0] - self.speed * self.dest[0]) * self.dist[0] <= 0:
                    x_move = self.dist[0]
                #else:
                 #   x_move = 0

                if (self.dist[1] - self.speed * self.dest[1]) * self.dist[1] > 0:
                    y_move = self.speed * self.dest[1]
                elif (self.dist[1] - self.speed * self.dest[1]) * self.dist[1] <= 0:
                    y_move = self.dist[1]
                #else:
                 #   y_move = self.dist
                # print(self.dist, (self.dist[1] - self.speed * self.dest[1]) * self.dist[1])
                elem.move(x_move, y_move)
                elem.draw(screen)
            self.dist[0] -= x_move
            self.dist[1] -= y_move
            if self.dist[0] == 0 and self.dist[1] == 0:
                self.amount -= 1
                self.current_position = (self.current_position + 1) % 2
                if self.amount == 0:
                    for e in self.sprites:
                        e.draw(screen)
                    self.moving = False
                    self.pos, self.get_to = self.get_to, self.pos
                else:
                    self.current_position = (self.current_position + 1) % 2
                    self.move(self.amount - 1, self.next_sprites)
        else:
            for e in self.sprites:
                e.draw(screen)


class Animator:
    """Класс-аниматор"""

    def __init__(self, path, options=None):
        # создаем словарь вида {имя анимации: [список из pygame.Surface]}
        self.animations = {i: [load_image(path + '/' + i + '/' + k)
                               for k in os.listdir(path + '/' + i)]
                           for i in os.listdir(path)}
        self.animation = 'idle'  # по умолчанию стоит анимация покоя
        self.counter = 0  # текущий кадр анимации
        self.sub_counter = 0  # сколько тактов будет отображаться каждй кадр

        self.static = options.get('static', False) if options else False
        # статичность картинки
        self.max_sub_counter = options.get('speed', 2) if options else 2
        # задержка между кадрами анимации
        self.cycle = options.get('cycle', False) if options else False
        # цикличность анимации

        #self.shift = (0, 0)  # смещение спрайта при некоторых анимациях

    def next_(self):
        """Следущий кадр анимации"""
        if not self.static:
            self.sub_counter += 1
            if self.sub_counter == self.max_sub_counter:
                # делаем задержку между кадрами анимации
                self.counter += 1
                self.sub_counter = 0
            if self.counter >= len(self.animations[self.animation]):
                # если закончили проигрывать текущую анимацию
                if self.animation == 'die':
                    # чтобы после анимации смерти не включалась анимация покоя
                    self.counter -= 1
                else:
                    if self.cycle:
                        # если анимация циклическая, то заново её запускаем
                        self.start(self.animation)
                    else:
                        self.start('idle')
        # возвращаем кадр и смещение
        return self.animations[self.animation][self.counter] #, self.shift

    def start(self, name):
        """Начать новую анимацию"""
        if name not in self.animations.keys():
            return  # если такой анимации не существует

        self.animation = name  # меняем имя анимации
        self.counter = 0  # обнуляем счетчик кадров
        self.sub_counter = 0  # обнуляем задержку
     #   # для некоторых анимаций необходимо смещение спрайта,
     #   # чтобы они корректно отображались
     #   if name == 'move_right':
     #       self.shift = (-TILE, 0)
     #   elif name == 'move_down':
     #       self.shift = (0, -TILE)
     #   elif name == 'attack_left':
     #       self.shift = (-TILE, 0)
     #   elif name == 'attack_up':
     #       self.shift = (0, -TILE)
     #   else:
     #       self.shift = (0, 0)

def change_info(moving_sprite_group, id_to_select):
    if id_to_select != 0:
        if not moving_sprite_group.moving:
            try:
                moving_sprite_group.sprites[0].change_pic("resources/buildings/" + str(id_to_select) + '.png')
            except Exception:
                moving_sprite_group.sprites[0].change_pic("resources/buildings/" + str(id_to_select) + '.jpg')
            for i in range(2, len(moving_sprite_group.sprites)):
                text = (buildings_db[id_to_select - 1][i - 1])
                if i > 3:
                    text *= -1
                    if text > 0:
                        text = '+' + str(text)
                moving_sprite_group.sprites[i].set_text(text, 'red')
                moving_sprite_group.move(1 + moving_sprite_group.current_position, moving_sprite_group.sprites)
        else:
            try:
                moving_sprite_group.next_sprites[0].change_pic("resources/buildings/" + str(id_to_select) + '.png')
            except Exception:
                moving_sprite_group.next_sprites[0].change_pic("resources/buildings/" + str(id_to_select) + '.jpg')
            for i in range(2, len(moving_sprite_group.next_sprites)):
                text = (buildings_db[id_to_select - 1][i - 1])
                if i > 3:
                    text *= -1
                    if text > 0:
                        text = '+' + str(text)
                moving_sprite_group.next_sprites[i].set_text(text, 'red')
                moving_sprite_group.move(1 + moving_sprite_group.current_position, moving_sprite_group.next_sprites)
        #else:
        #    moving_sprite_group.move(1 + moving_sprite_group.current_position, moving_sprite_group.sprites)
    else:
        if moving_sprite_group.current_position != 0:
            moving_sprite_group.move()