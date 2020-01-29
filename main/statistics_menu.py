import pygame as pg
from main.objects.buttons import ButtonGetLevelMenu
from main.objects.group_sprites import all_sprites
from main.delete_all_sprites import delete_all_sprites
from main.window import screen
from main.objects.cursor import Cursor
import sqlite3

class StatisticsMenu:
    def __init__(self, level):
        delete_all_sprites()
        self.btn_get_lvl_menu = ButtonGetLevelMenu(300, 550, move=True, speed_y=15)
        self.level = level
        pg.font.init()
        self.cursor = Cursor()
        self.font = pg.font.SysFont('arial', 16)
        self.times = []
        self.get_text()
        self.render_text()
        self.run()


    def get_text(self):
        con = sqlite3.connect('statistics.db')
        cur = con.cursor()
        self.times = cur.execute(f'SELECT travel_time FROM travel WHERE level == {self.level}').fetchall()
        self.times = set(map(lambda x: (x[0], int(''.join(x[0].split(':')))), self.times))
        self.times = sorted(self.times, key=lambda x: x[0], reverse=True)

    def render_text(self):
        for time in self.times:
            text = self.font.render(f'{self.times.index(time) + 1}. {time[0]}', 1, (7, 85, 30))
            sprite = pg.sprite.Sprite()
            sprite.image = text
            sprite.rect = sprite.image.get_rect().move(0, self.times.index(time) * 30)
            all_sprites.add(sprite)

    def run(self):
        running = True
        while running:
            for event in pg.event.get():
                if event == pg.QUIT:
                    quit()
                all_sprites.update(event)
            screen.fill((0, 198, 255))
            self.cursor.update(self.btn_get_lvl_menu, n=-275)
            for sprite in all_sprites:
                self.cursor.apply(sprite)
            all_sprites.draw(screen)
            pg.display.flip()

            if self.btn_get_lvl_menu.menu_close_open[0] == True:
                menu_close_open = self.btn_get_lvl_menu.menu_close_open
                running = False

        if menu_close_open[1] == 'btn_get_lvl_menu':
            from main.level_menu import LevelMenu
            LevelMenu()
