import pygame as pg
from main.objects.tiles import tiles_group, move_up_tiles_group, \
    move_down_tiles_group, move_left_tiles_group, \
    move_right_tiles_group, jump_tiles_group, \
    finish_tiles_group
from main.objects.skin import Skin
from main.window import all_sprites
player_group = pg.sprite.Group()
# player_image = pg.image.load('textures/player.png')
player_image = pg.image.load('C:/Users/poel/PycharmProjects/tap_tap_dash/textures/player.png')


class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)

        tile_width = tile_height = 64
        self.image = player_image
        self.speed = 4
        self.rect = self.image.get_rect().move(tile_width * pos_x + 28, tile_height * pos_y + 28)
        self.mode = 'run'
        self.n = 0  # угол для class Skin
        self.lvl = 0  # удалить
        self.check(0)
        self.time_start = 0
        self.skin = Skin(self.rect.x, self.rect.y)

    def move(self):
        if pg.sprite.spritecollideany(self.skin, tiles_group) or 0 < pg.time.get_ticks() - self.time_start <= 500:
            self.rect.y += self.speed_y
            self.rect.x += self.speed_x
        elif pg.sprite.spritecollide(self.skin, finish_tiles_group, False):
            self.data_output(('playing', 'lvl'), (False, self.lvl + 1))
        else:
            self.data_output(('playing', 'restart_menu'), (False, True))

        if 0 < pg.time.get_ticks() - self.time_start > 500:
            self.mode = 'run'
            self.skin.rotate_skin(self.n, self.mode)

    def check(self, angle):
        if angle == 0:
            self.speed_y = -self.speed
            self.speed_x = 0
        elif angle == 180:
            self.speed_y = self.speed
            self.speed_x = 0
        elif angle == 90:
            self.speed_x = -self.speed
            self.speed_y = 0
        elif angle == 270:
            self.speed_x = self.speed
            self.speed_y = 0

    def update(self, *args):
        if args[0].type == pg.MOUSEBUTTONDOWN:
            if pg.sprite.spritecollideany(self, move_up_tiles_group):
                self.n = 0
                self.check(0)
                self.skin.rotate_skin(0, self.mode)
            elif pg.sprite.spritecollideany(self, move_down_tiles_group):
                self.n = 180
                self.check(180)
                self.skin.rotate_skin(180, self.mode)
            elif pg.sprite.spritecollideany(self, move_left_tiles_group):
                self.n = 90
                self.check(90)
                self.skin.rotate_skin(90, self.mode)
            elif pg.sprite.spritecollideany(self, move_right_tiles_group):
                self.n = 270
                self.check(270)
                self.skin.rotate_skin(270, self.mode)
            else:
                self.data_output(('playing', 'restart_menu'), (False, True))

            if pg.sprite.spritecollide(self, jump_tiles_group, False):
                self.time_start = pg.time.get_ticks()
                self.mode = 'fly'
                self.skin.rotate_skin(self.n, self.mode)

    def data_output(self, keys, value):
        global DICT_DATA
        dict_data = DICT_DATA.copy()
        for ind_key in range(len(keys)):
            dict_data[keys[ind_key]] = value[ind_key]
        return dict_data
