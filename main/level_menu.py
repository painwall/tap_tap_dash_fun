import pygame as pg
from main.objects.buttons import ButtonGetLevel, ButtonGetStartMenu
from main.window import clock, screen
from main.objects.group_sprites import all_sprites, offset_x_group
from main.delete_all_sprites import delete_all_sprites
from main.objects.scrollbar import Scrollbar
import traceback
import os


class LevelMenu:
    def __init__(self):
        delete_all_sprites()
        self.list_levels = [ButtonGetLevel(x * 60 + 300, 250, os.listdir('levels')[x],
                                           (all_sprites, offset_x_group)) for x in
                            range(len(os.listdir('levels')))]

        self.btn_get_initial_menu = ButtonGetStartMenu(300, 375, (all_sprites,))
        self.scrollbar = Scrollbar(0, 0, (offset_x_group,), offset_x=True)
        self.run()

    def run(self):
        running = True
        while running:
            screen.fill((0, 198, 255))
            # clock.tick(120)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                all_sprites.update(event)
                self.scrollbar.update(event)

            all_sprites.draw(screen)
            pg.display.flip()
            if self.btn_get_initial_menu.menu_close_open[0]:
                menu_close_open = self.btn_get_initial_menu.menu_close_open
                running = False
            for btn_lvl in self.list_levels:
                if btn_lvl.menu_close_open[0]:
                    menu_close_open = btn_lvl.menu_close_open
                    running = False
        try:
            if menu_close_open[1] == 'initial_menu':
                from main.initial_menu import InitialMenu
                InitialMenu()
            elif menu_close_open[1] == 'play':
                from main.playing import Play
                print(menu_close_open[2])
                Play(menu_close_open[2])

            elif menu_close_open[1] == 'statistics':
                from main.statistics_menu import StatisticsMenu
                print(menu_close_open)
                StatisticsMenu(menu_close_open[2])
        except BaseException:
            print('Ошибка:\n', traceback.format_exc())
