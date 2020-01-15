import pygame as pg
import random
import os
from main.window import clock, screen
from main.initial_menu import InitialMenu
# группы спрайтов и загрузка первыъ изображений
move_tile_image = pg.image.load('textures/tile_move.png')
DICT_DATA = {'playing': False, 'lvl_menu': False,
             'lvl': False, 'initial_menu': False,
             'restart_menu': False}

PLAY = False
LVL_MENU = False
LVL = 0
START_MENU = True
MENU = False

InitialMenu()

while True:
    screen.fill((0, 198, 255))
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    pg.display.flip()
