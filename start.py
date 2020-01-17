import pygame as pg
from main.window import clock, screen
from main.initial_menu import InitialMenu
# группы спрайтов и загрузка первыъ изображений
move_tile_image = pg.image.load('textures/tile_move.png')
DICT_DATA = {'playing': False, 'lvl_menu': False,
             'lvl': False, 'initial_menu': False,
             'restart_menu': False}

InitialMenu()

while True:
    screen.fill((0, 198, 255))
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
    pg.display.flip()
