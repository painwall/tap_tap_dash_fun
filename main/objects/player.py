import pygame as pg
from main.objects.tiles import tiles_group, finish_tiles_group
from main.objects.skin import Skin
from main.window import all_sprites
player_group = pg.sprite.Group()
# player_image = pg.image.load('textures/player.png')
player_image = pg.image.load('textures/player.png')


class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)

        tile_width = tile_height = 64
        self.image = player_image
        self.speed = 1
        self.rect = self.image.get_rect().move(tile_width * pos_x + 28, tile_height * pos_y + 28)
        self.mode = 'run'
        self.n = 0  # угол для class Skin
        self.direction_of_movement(0)
        self.menu_close_open = (False,)
        self.time_start = 0
        self.skin = Skin(self.rect.x, self.rect.y)

    def move(self):
        if pg.sprite.spritecollideany(self.skin, tiles_group) or (0 < pg.time.get_ticks() - self.time_start <= 500):
            self.rect.y += self.speed_y
            self.rect.x += self.speed_x
        if pg.sprite.spritecollide(self.skin.image, finish_tiles_group, False):
            self.check(True, 'new_level')
        else:
            self.check(True, 'restart_menu')

        if 0 < pg.time.get_ticks() - self.time_start > 500:
            self.mode = 'run'
            self.skin.rotate_skin(self.n, self.mode)

    def direction_of_movement(self, angle):
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
        if args[0].type == pg.KEYUP:
            if args[0].key == 273:
                self.n = 0
                self.direction_of_movement(0)
                self.skin.rotate_skin(0, self.mode)
            elif args[0].key == 274:
                self.n = 180
                self.direction_of_movement(180)
                self.skin.rotate_skin(180, self.mode)
            elif args[0].key == 276:
                self.n = 90
                self.direction_of_movement(90)
                self.skin.rotate_skin(90, self.mode)
            elif args[0].key == 275:
                self.n = 270
                self.direction_of_movement(270)
                self.skin.rotate_skin(270, self.mode)
            else:
                self.check(True, 'restart_menu')


            if args[0].key ==32:
                self.time_start = pg.time.get_ticks()
                self.mode = 'fly'
                self.skin.rotate_skin(self.n, self.mode)

    def check(self, booll, name_menu):
        self.menu_close_open = (booll, name_menu)
