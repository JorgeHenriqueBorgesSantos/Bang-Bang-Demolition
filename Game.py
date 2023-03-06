import pygame
from Config import *
from Players import *
from Bullet import *

pygame.init()
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bang Bang Demolition")

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

shooter_sprites = pygame.sprite.Group()
shooter_1_game = Shooter(shooter_1, 50, 510)
shooter_2_game = Shooter(shooter2, 910, 510)
coord = [[500, 375], [50, 165], [910, 165], [910, 547]]
shooter_sprites.add(shooter_1_game, shooter_2_game)
hit_timer = 0

def bullet_collision(shooter_one, shooter_two):

    if shooter_two.stop:
        return

    for bullet in shooter_two.cartridge:
        if pygame.sprite.collide_mask(bullet, shooter_one):
            tank_two.ball_list.remove(bullet)
            cartridge.empty()
            game.hit_timer = defeat_time
            game.coord = [[500, 375], [50, 165], [910, 165], [910, 547]]
            tank_one.hit = True
            tank_two.stop = True
            explosion_sound_effect.play()
