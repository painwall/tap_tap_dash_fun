import pygame as pg
from main.objects.buttons import ButtonGetLevel, ButtonGetStartMenu
from main.window import clock, screen
from main.objects.group_sprites import all_sprites, offset_x_group
from main.delete_all_sprites import delete_all_sprites
from main.objects.scrollbar import Scrollbar
from main.objects.label import Label
import traceback
import os


class LevelMenu:
    def __init__(self):
        delete_all_sprites()
        self.list_levels = [ButtonGetLevel(x * 60 + 300, 250, os.listdir('levels')[x],
                                           (all_sprites, offset_x_group)) for x in
                            range(len(os.listdir('levels')))]

        self.btn_get_initial_menu = ButtonGetStartMenu(300, 375, (all_sprites,))
        self.labels = {'help': Label(all_sprites, (550, 540), (235, 100), background=(0, 198, 255),
                                     text='ПКМ - открытие статистики\n'
                                          'ЛКМ - запустить уровень\n'
                                          'Колёсико мыши - перемещение уровней')}
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
            if self.btn_get_initial_menu.event[0]:
                event = self.btn_get_initial_menu.event
                running = False
            for btn_lvl in self.list_levels:
                if btn_lvl.event[0]:
                    event = btn_lvl.event
                    running = False
        try:
            if event[1] == 'initial_menu':
                from main.initial_menu import InitialMenu
                InitialMenu()
            elif event[1] == 'play':
                from main.playing import Play
                print(event[2])
                Play(event[2])

            elif event[1] == 'statistics':
                from main.statistics_menu import StatisticsMenu
                print(event)
                StatisticsMenu(event[2])
        except BaseException:
            print('Ошибка:\n', traceback.format_exc())
