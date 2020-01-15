import pygame as pg
from main.window import all_sprites
skin_group = pg.sprite.Group()

class Skin(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(skin_group, all_sprites)
        self.start_image = pg.image.load('textures/bird.png')
        self.start_image_fly = pg.image.load('textures/fly_bird.png')
        self.image = pg.image.load('textures/bird.png')
        self.rect = self.image.get_rect().move(x - 28, y - 28)

    def move(self):
        self.rect.x = player.rect.x - 28
        self.rect.y = player.rect.y - 28

    def rotate_skin(self, n, mode):
        if mode == 'run':
            self.image = pg.transform.rotate(self.start_image, n)
        elif mode == 'fly':
            self.image = pg.transform.rotate(self.start_image_fly, n)