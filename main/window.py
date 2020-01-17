import pygame as pg
from .objects.camera_and_cursor import Camera

WIN_WIDTH = 800
WIN_HEIGHT = 600
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
camera = Camera()
all_sprites = pg.sprite.Group()
