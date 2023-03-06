import math
import Game
import random

import pygame.sprite
from Config import *
from Bullet import *


class Shooter(pygame.sprite.Sprite):
    def __init__(self, sprite, pos_x, pos_y):
        super().__init__()
        self.score = 0
        self.cartridge = []
        self.rect = self.image.get_rect
        self.x = pos_x
        self.y = pos_y
        self.rotation = 0
        self.move_W = False
        self.move_S = False
        self.shoot = False
        self.hit = False
        self.stop = False
        self.shoot_time = 0

    def shot(self):
        self.shoot = True

    def rotate(self, rotate):
        self.rotation = rotate

    def update(self):
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.bullet_list()

        if (self.hit) and Game.hit_timer <= 0:
            self.stop = False
            self.hit = False
            choice = random.choice(Game.coord)
            Game.coord.remove(choice)
            self.x = choice[0]
            self.y = choice[1]

        if self.stop:
            return

        self.shoot_time -= 1

    def bullet_update(self):
        for bullet in self.cartridge:
            for i in range(0, bullet_speed):
                Bullet.movement()
                Bullet.collision()

            if Bullet.cont >= bullet_bounce:
                self.cartridge.remove(bullet)
                Game.bullet_sprites.remove(bullet)

    def collision(self):
        for wall in Game.walls:
            if pygame.sprite.collide_mask(self, wall):
                # top wall
                if abs(self.rect.top - wall.rect.bottom) < 25:
                    self.y += shooter_speed
                # bottom wall
                elif abs(wall.rect.top - self.rect.bottom) < 25:
                    self.y += shooter_speed
                # left wall
                elif abs(wall.rect.left - self.rect.right) < 25:
                    self.x += shooter_speed
                # right wall
                elif abs(self.rect.left - wall.rect.right) < 25:
                    self.x += shooter_speed
