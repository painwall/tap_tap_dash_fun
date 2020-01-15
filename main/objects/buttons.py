import pygame as pg
from main.window import all_sprites


class ButtonGetLevel(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, number):
        super().__init__(all_sprites)
        pg.font.init()
        surf = pg.Surface((50, 50))
        surf.fill((0, 198, 255))
        pg.draw.circle(surf, (255, 255, 255), (25, 25), 25)
        font = pg.font.SysFont('arial', 16)
        text = font.render(f'{number}', 1, (7, 85, 30))
        surf.blit(text, (int((50 - text.get_width()) / 2), 15))
        self.level = int(number)
        self.image = surf
        surf_final = pg.Surface((50, 50))
        surf_final.fill((0, 198, 255))
        pg.draw.circle(surf_final, (73, 67, 67), (25, 25), 25)
        surf_final.blit(text, (int((50 - text.get_width()) / 2), 15))
        self.final_image = surf_final
        self.rect = self.image.get_rect().move(pos_x * 60, pos_y)
        self.menu_close_open = (False,)
        print('все норм')

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
            self.check()

    def check(self):
        self.menu_close_open = (True, 'play', self.level)


class ButtonGetStartMenu(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = pg.image.load('../textures/btn_menu_start.png')
        self.final_image = pg.image.load('../textures/btn_menu_final.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.speed_x = 1
        self.menu_close_open = (False,)
        self.end_coord_x = self.rect.x

    def move(self):
        if self.end_coord_x > self.rect.x:
            self.rect.x += self.speed_x
        elif self.end_coord_x < self.rect.x:
            self.rect.x -= self.speed_x

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]

        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 3:
            self.end_coord_x = pg.mouse.get_pos()[0]
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
            self.check()
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 4 and self.speed_x <= 5:
            self.speed_x += 1
        elif args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 5 and self.speed_x > 0:
            self.speed_x -= 1

    def check(self):
        self.menu_close_open = (True, 'initial_menu')


class ButtonGetLevelMenu(pg.sprite.Sprite):
    def __init__(self, start_image, final_image, x, y):
        super().__init__(all_sprites)
        self.final_image = pg.image.load(final_image)
        self.image = pg.image.load(start_image)
        self.menu_close_open = ('False',)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        global LVL_MENU
        global START_MENU
        global MENU
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
            self.check()

    def check(self):
        self.menu_close_open = (True, 'btn_get_lvl_menu')


class ButtonGetSkins(pg.sprite.Sprite):
    def __init__(self, start_image, final_image, x, y):
        super().__init__(all_sprites)
        self.final_image = pg.image.load(final_image)
        self.image = pg.image.load(start_image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self):
        self.image = pg.image.load()

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image


class ButtonRestart(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.final_image = pg.image.load('textures/btn_restart_final.png')
        self.image = pg.image.load('textures/btn_restart_start.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self):
        self.image = pg.image.load()

    def update(self, *args):
        global PLAY
        global MENU
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
