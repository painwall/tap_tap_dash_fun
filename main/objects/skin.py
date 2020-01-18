import pygame as pg
from main.window import all_sprites
from main.objects.animated_sprite import AnimatedSprite
from main.objects.group_sprites import skin_group


class Skin(AnimatedSprite):
    def __init__(self, x, y, speed):
        super().__init__(pg.image.load('textures/hero.png'), 9, 1, 64, 64,
                         skin_group, all_sprites)

        self.delay_animation = 100
        self.time = 0
        self.angle = 0
        self.rect = self.image.get_rect().move(x, y)

    def move(self, x, y):
        self.rect.x = x - 28
        self.rect.y = y - 128