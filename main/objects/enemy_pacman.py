import pygame as pg
from main.objects.group_sprites import enemy_group, all_sprites


class EnemyPacman(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(enemy_group)

