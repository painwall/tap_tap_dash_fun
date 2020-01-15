import pygame as pg
from start import screen, all_sprites, clock
from .objects.buttons import ButtonGetLevelMenu, ButtonRestart

class RestartMenu:
    def __init__(self):
        pass

    def run(self):
        delete_all_sprites()
        ButtonGetLevelMenu('textures/btn_lvls_start.png', 'textures/btn_lvls_final.png', 300, 275)
        ButtonRestart(300, 375)
        while MENU:
            screen.fill((0, 198, 255))
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    all_sprites.update(event)
            all_sprites.draw(screen)
            pg.display.flip()