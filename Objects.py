import pygame
from config import *


def sign(num):
    return -1 if num < 0 else 1


class GroupMoving:
    def __init__(self, sprite_group, start_pos, end_pos, speed):
        self.sprites = sprite_group
        self.pos = start_pos
        self.get_to = end_pos
        self.moving = False
        self.speed = speed

    def move(self, sprite_group=None):
        if not self.moving:
            if sprite_group is not None:
                self.sprites = sprite_group
            self.moving = True
            self.dest = (sign(self.pos[0] - self.get_to[0]) * -1,
                     sign(self.pos[1] - self.get_to[1]) * -1)
            self.dist = [(self.pos[0] - self.get_to[0]) * -1, (self.pos[1] - self.get_to[1]) * -1]

    def update(self, screen):
        if self.moving:
            for elem in self.sprites:
                if (self.dist[0] - self.speed * self.dest[0]) * self.dist[0] > 0:
                    x_move = self.speed * self.dest[0]
                elif (self.dist[0] - self.speed * self.dest[0]) * self.dist[1] < 0:
                    x_move = self.dist[0]
                else:
                    x_move = 0

                if (self.dist[1] - self.speed * self.dest[1]) * self.dist[1] > 0:
                    y_move = self.speed * self.dest[1]
                elif (self.dist[1] - self.speed * self.dest[1]) * self.dist[1] < 0:
                    y_move = self.dist[1]
                else:
                    y_move = 0

                self.dist[0] -= x_move
                self.dist[1] -= y_move
                elem.move(x_move, y_move)
                elem.draw(screen)
            if self.dist[0] == 0 and self.dist[1] == 0:
                self.moving = 0
                self.pos, self.get_to = self.get_to, self.pos
        else:
            for e in self.sprites:
                e.draw(screen)
