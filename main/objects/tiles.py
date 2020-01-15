import pygame as pg
from main.window import all_sprites

tiles_group = pg.sprite.Group()
finish_tiles_group = pg.sprite.Group()
move_up_tiles_group = pg.sprite.Group()
move_down_tiles_group = pg.sprite.Group()
move_left_tiles_group = pg.sprite.Group()
move_right_tiles_group = pg.sprite.Group()
jump_tiles_group = pg.sprite.Group()
move_tile_image = pg.image.load('textures/tile_move.png')

class Tile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        tile_width = tile_height = 32 * 2
        self.image = pg.image.load('textures/tile1.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class MoveUpTile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, move_up_tiles_group)
        tile_width = tile_height = 32 * 2
        self.image = move_tile_image
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class MoveDownTile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, move_down_tiles_group)
        tile_width = tile_height = 32 * 2
        self.image = pg.transform.rotate(move_tile_image, 180)
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class MoveLeftTile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, move_left_tiles_group)
        tile_width = tile_height = 32 * 2
        self.image = pg.transform.rotate(move_tile_image, 90)
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class MoveRightTile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, move_right_tiles_group)
        tile_width = tile_height = 32 * 2
        self.image = pg.transform.rotate(move_tile_image, 270)
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class JumpTile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, jump_tiles_group)
        tile_width = tile_height = 32 * 2
        self.image = pg.image.load('textures/tile_jump.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class FinishTile(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, finish_tiles_group)
        tile_width = tile_height = 32 * 2
        self.image = pg.image.load('textures/tile_finish.png')
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
