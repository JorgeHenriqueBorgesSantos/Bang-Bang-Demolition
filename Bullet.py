import pygame
from Config import thud_sound_effect


class Bullet(pygame.sprite.Sprite):

    def __init__(self, shooter_x, shooter_y, spd_x, spd_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = shooter_x
        self.y = shooter_y
        self.cont = 0
        self.image = pygame.image.load('Sprites/ball.png')
        # self.image = pygame.transform.scale(self.image, (8 * 5, 8 * 5))
        self.group = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.dx = spd_x
        self.dy = spd_y

    def movement(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def collision(self, walls):
        for wall in walls:
            if pygame.sprite.collide_mask(self, wall):
                thud_sound_effect.set_volume(0.4)
                thud_sound_effect.play()
                # top wall collision
                if abs(self.rect.top - wall.rect.bottom) < 25 and self.dy < 0:
                    self.dy *= -1
                # bottom wall collision
                elif abs(wall.rect.top - self.rect.bottom) < 25 and self.dy > 0:
                    self.dy *= -1
                # left wall collision
                elif abs(wall.rect.left - self.rect.right) < 25 and self.dx > 0:
                    self.dx *= -1
                # right wall collision
                elif abs(self.rect.left - wall.rect.right) < 25 and self.dx < 0:
                    self.dx *= -1
                self.cont += 1
