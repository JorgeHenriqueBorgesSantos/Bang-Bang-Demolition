import pygame

pygame.font.init()
pygame.mixer.init()

# Screen
score_height = 50
wall_width = 25
screen_width = 1000
screen_height = 750

# Colors
red = (134, 28, 9)
yellow = (212, 169, 65)
white = (255, 255, 255)
green = (0, 127, 33)
purple = (104, 15, 133)
# DARKER_GREEN = (31, 61, 12)
# DARKER_BLUE = (11, 11, 69)

# Rectangles constant
rect_1 = (25, 25)

# Screen refresh
fps = 60

# Wall group
walls = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()

tam_player = 32

# Clock
clock = pygame.time.Clock()

# Game
stun_time = 50

# Tanks
shooter_1 = pygame.image.load("Sprites/Shooter_1.png")
shooter_2 = pygame.image.load("Sprites/Shooter_2.png")
rot_speed = 0.4
shooter_speed = 3
bullet_speed = 3
bullet_bounce = 2

shot_time = 10

# Sounds
thud_sound_effect = pygame.mixer.Sound("Sounds/Thud.wav")
shot_sound_effect = pygame.mixer.Sound("Sounds/Shot.wav")
explosion_sound_effect = pygame.mixer.Sound("Sounds/explosion.wav")
