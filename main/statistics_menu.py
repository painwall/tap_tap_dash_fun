import pygame as pg
from main.objects.buttons import ButtonGetLevelMenu
from main.objects.group_sprites import all_sprites, offset_y_group, statistical_time_group
from main.delete_all_sprites import delete_all_sprites
from main.window import screen
from main.objects.scrollbar import Scrollbar
from main.objects.statistical_time import StatisticalTime
from main.objects.check_box import CheckBox
from main.objects.label import Label
import sqlite3


class StatisticsMenu:
    def __init__(self, level):
        delete_all_sprites()
        self.btn_get_lvl_menu = ButtonGetLevelMenu(300, 550, (all_sprites,))
        self.level = level
        self.scrollbar = Scrollbar(790, 0, (offset_y_group,), offset_y=True)
        self.check_box = CheckBox((730, 500), (all_sprites,))
        self.labels = {
            'Your_statictics': Label((all_sprites, offset_y_group), (265
                                                                     , 0),
                                     (270, 72 * 1.338307),
                                     background=(0, 198, 255),
                                     text='Статистика уровня\n          (Время)',
                                     size_font=36),
            'View_full_statictics': Label(all_sprites, (550, 522), (180, 25),
                                          background=(0, 198, 255),
                                          text='Показать полную статистику',
                                          size_font=16),
            'Help': Label(all_sprites, (600, 570), (200, 20),
                          background=(0, 198, 225),
                          text='Колесико мыши для просмотра выше/ниже')
        }
        with open('data/accounts/id_account.txt') as txt:
            self.id_account = int(txt.read())
        self.times = []
        self.get_text()
        self.run()

    def get_text(self):
        con = sqlite3.connect('data/statistics.db')
        cur = con.cursor()
        con_account = sqlite3.connect('data/accounts/accounts.db')
        cur_account = con_account.cursor()
        if self.check_box.flag:
            self.times = cur.execute(f'SELECT travel_time, id_account'
                                     f' FROM travel WHERE'
                                     f' level == {self.level}').fetchall()
        else:
            self.times = cur.execute(f'SELECT travel_time, id_account'
                                     f' FROM travel WHERE'
                                     f' level == {self.level}'
                                     f' and id_account={self.id_account}').fetchall()
        self.times = set(map(lambda x: (x[0], x[1], int(''.join(x[0].split(':')))), self.times))
        print(self.times, 'check')
        self.times = sorted(self.times, key=lambda x: x[-1])
        dict_accounts = {}
        for el in self.times:
            try:
                dict_accounts[str(el[1])] = str(cur_account.execute(f'SELECT account_name'
                                                                    f' FROM accounts'
                                                                    f' WHERE id={el[1]}').fetchone()[0])
            except TypeError:
                pass
        print(dict_accounts)
        self.create_times(dict_accounts)

    def create_times(self, dict_accounts):
        for sprite in statistical_time_group:
            sprite.kill()

        for time in self.times:
            if self.check_box.flag:
                try:
                    StatisticalTime(30, self.times.index(time) * 30 + 100,
                                    self.times.index(time) + 1, f'{time[0]} - {str(dict_accounts[str(time[1])])}',
                                    (all_sprites, offset_y_group, statistical_time_group))
                except KeyError:
                    StatisticalTime(30, self.times.index(time) * 30 + 100,
                                    self.times.index(time) + 1, f'{time[0]} - Удаленный аккаунт',
                                    (all_sprites, offset_y_group, statistical_time_group))
            else:
                StatisticalTime(30, self.times.index(time) * 30 + 100, self.times.index(time) + 1, time[0],
                                (all_sprites, offset_y_group, statistical_time_group))

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
            if self.check_box.event[0]:
                self.get_text()
                self.check_box.event = (False,)

        if event[1] == 'btn_get_lvl_menu':
            from main.level_menu import LevelMenu
            LevelMenu()
