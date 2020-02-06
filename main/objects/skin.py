import pygame as pg
from main.objects.group_sprites import all_sprites

from main.objects.animated_sprite import AnimatedSprite
from main.objects.group_sprites import skin_group


class Skin(AnimatedSprite):
    def __init__(self, x, y, speed, time_fly):
        super().__init__([pg.image.load('textures/hero_run.png'), pg.image.load('textures/hero_fly.png')],
                         (9, 7), (1, 1), 64, 64,
                         skin_group, all_sprites)

        self.delay_animation = [(speed + 300) / 4.5, time_fly / 6]
        self.time = 0
        self.angle = 0
        self.rect = self.image.get_rect().move(x, y)

    def move(self, x, y):
        self.rect.x = x - 14
        self.rect.y = y - 116