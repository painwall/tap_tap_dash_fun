import pygame as pg
from main.objects.buttons import ButtonGetLevelMenu
from main.objects.group_sprites import all_sprites, offset_y_group
from main.delete_all_sprites import delete_all_sprites
from main.window import screen
from main.objects.scrollbar import Scrollbar
from main.objects.statistical_time import StatisticalTime
from main.objects.check_box import CheckBox
import sqlite3


class StatisticsMenu:
    def __init__(self, level):
        delete_all_sprites()
        self.btn_get_lvl_menu = ButtonGetLevelMenu(300, 550, (all_sprites,))
        self.level = level
        self.scrollbar = Scrollbar(790, 0, (offset_y_group,), offset_y=True)
        self.check_box = CheckBox((500, 500), (all_sprites,))
        with open('data/accounts/id_account.txt') as txt:
            self.id_account = int(txt.read())
        self.times = []
        self.get_text()
        self.run()

    def get_text(self):
        con = sqlite3.connect('data/statistics.db')
        cur = con.cursor()
        self.times = cur.execute(f'SELECT travel_time'
                                 f' FROM travel WHERE'
                                 f' level == {self.level}'
                                 f' and id_account={self.id_account}').fetchall()
        self.times = set(map(lambda x: (x[0], int(''.join(x[0].split(':')))), self.times))
        self.times = sorted(self.times, key=lambda x: x[0])
        self.create_times()

    def create_times(self):
        for time in self.times:
            StatisticalTime(0, self.times.index(time) * 30, self.times.index(time) + 1, time[0],
                            (all_sprites, offset_y_group))

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                all_sprites.update(event)
                self.scrollbar.update(event)
            screen.fill((0, 198, 255))
            all_sprites.draw(screen)
            pg.display.flip()

            if self.btn_get_lvl_menu.event[0]:
                event = self.btn_get_lvl_menu.event
                running = False

        if event[1] == 'btn_get_lvl_menu':
            from main.level_menu import LevelMenu
            LevelMenu()
