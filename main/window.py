import pygame as pg
from  .objects.camera_and_cursor import Camera

#_______
WIN_WIDTH = 800
WIN_HEIGHT = 600
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
camera = Camera()
#_____
all_sprites = pg.sprite.Group()
