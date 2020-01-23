import pygame as pg
from main.objects.group_sprites import enemy_group, all_sprites


class EnemyPacman(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__(enemy_group, all_sprites)
        tile_width = tile_height = 64
        self.speed = 1
        self.image = pg.image.load('textures/1.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x + 14, tile_height * pos_y + 14)

    def direction_of_movement(self):
        pass

