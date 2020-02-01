import pygame as pg
from main.objects.group_sprites import scrollbar_group


class Scrollbar(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, groups_sprites, offset_x=False, offset_y=False):
        super().__init__(scrollbar_group)
        self.rect = (pos_x, pos_y, 10, 10)
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.groups_sprites = groups_sprites
        self.speed_x = 10
        self.speed_y = 10
        surf = pg.Surface((10, 10))
        self.image = surf

    def update_sprites(self):
        for sprite_group in self.groups_sprites:
            for sprite in sprite_group:
                if self.offset_x:
                    sprite.rect.x += self.speed_x
                if self.offset_y:
                    sprite.rect.y += self.speed_y

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN:
            if args[0].button == 4:
                if self.offset_x:
                    self.speed_x = abs(self.speed_x)
                elif self.offset_y:
                    self.speed_y = abs(self.speed_y)
                self.update_sprites()
            elif args[0].button == 5:
                if self.offset_x:
                    self.speed_x = -abs(self.speed_x)
                elif self.offset_y:
                    self.speed_y = -abs(self.speed_y)
                self.update_sprites()