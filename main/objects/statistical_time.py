import pygame as pg
from main.objects.group_sprites import statistical_time_group, all_sprites


class StatisticalTime(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, number_row, data, groups):
        super().__init__(groups)
        pg.font.init()
        self.font = pg.font.SysFont('arial', 16)
        text = self.font.render(f'{number_row}. {data}', 1, (7, 85, 30))
        self.image = text
        self.rect = self.image.get_rect().move(pos_x, pos_y)