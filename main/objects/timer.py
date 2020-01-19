import pygame as pg
from main.objects.group_sprites import clock_group


class Timer(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(clock_group)
        self.image = pg.Surface((100, 50))
        self.rect = self.image.get_rect().move(x, y)
        pg.font.init()
        self.font = pg.font.SysFont('arial', 16)
        self.time_start = pg.time.get_ticks()
        self.time = 0

        self.text = self.font.render(f'{self.time_start - pg.time.get_ticks()}', 1, (7, 85, 30))
        self.update()

    def update(self, *args):
        self.image.fill((255, 255, 255))
        self.time = pg.time.get_ticks() - self.time_start
        self.text = self.font.render(f'{self.time // 60000}:{self.time // 1000}:{self.time % 1000}', 1, (7, 85, 30))
        self.image.blit(self.text, ((int((70 - self.text.get_width()) / 2), 15)))
