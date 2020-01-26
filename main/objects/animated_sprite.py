import pygame as pg
from main.objects.group_sprites import all_sprites
from main.objects.group_sprites import skin_group
from main.window import clock
class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, sheets, columns, rows, x, y, *group):
        super().__init__(group)
        self.frames = []
        for ind in range(len(sheets)):
            self.frames.append([])
            self.cut_sheet(sheets[ind], columns[ind], rows[ind])
        self.row = 0
        self.cur_frame = 0
        self.image = self.frames[self.row][self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pg.Rect(0, 0, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames[-1].append(sheet.subsurface(pg.Rect(
                    frame_location, self.rect.size)))

    def edit_row(self, row):
        if self.row != row:
            self.row = row
            self.cur_frame = 0

    def update(self, time=None, angle=None):
        # обновление картинок
        try:# используется для создания задержки в анимации
            if time - self.time >= self.delay_animation[self.row]:
                self.time = time
                self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.row])
                self.image = pg.transform.rotate(self.frames[self.row][self.cur_frame], self.angle)
        except IndexError:
            pass
        except BaseException:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.row][self.cur_frame]
