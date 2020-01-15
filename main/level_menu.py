import pygame as pg
from main.objects.buttons import ButtonGetLevel, ButtonGetStartMenu
from main.window import clock, screen, all_sprites
from main.objects.camera_and_cursor import Cursor
from main.delete_all_sprites import delete_all_sprites
from main.initial_menu import InitialMenu
from main.playing import Play
import os


class LevelMenu:
    def __init__(self):
        delete_all_sprites()
        self.list_levels = [ButtonGetLevel(x, 190, os.listdir('../levels')[x]) for x in
                            range(len(os.listdir('../levels')))]

        self.cur = Cursor()
        self.btn_get_initial_menu = ButtonGetStartMenu(0, 300)
        self.run()

    def run(self):
        running = True
        while running:
            screen.fill((0, 198, 255))
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if self.btn_get_initial_menu.menu_close_open[0] == True:
                    menu_close_open = self.btn_get_initial_menu.menu_close_open
                    running = False
                for btn_lvl in self.list_levels:
                    if btn_lvl.menu_close_open[0] == True:
                        menu_close_open = btn_lvl.menu_close_open
                        running = False
                all_sprites.update(event)

            self.cur.update(self.btn_get_initial_menu)
            self.btn_get_initial_menu.move()
            all_sprites.draw(screen)
            for sprite in all_sprites:
                self.cur.apply(sprite)
            pg.display.flip()
        try:
            if menu_close_open[1] == 'initial_menu':
                InitialMenu()
            if menu_close_open[1] == 'play':
                Play(menu_close_open[2])
        except BaseException:
            pass


LevelMenu()
