import pygame as pg
from main.objects.group_sprites import all_sprites
from main.objects.account import Account
import sqlite3


class Button(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, final_image, groups_sprites):
        super().__init__(groups_sprites)
        self.image = pg.image.load(image)
        self.final_image = pg.image.load(final_image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.menu_close_open = (False,)
        self.speed_x = 0
        self.speed_y = 0
        self.move = False  # может двигаться кнопка или нет

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]

        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
            self.check()
            self.run()
        if self.move and args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 4:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        elif self.move and args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 5:
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y

    def check(self):
        pass

    def run(self):
        pass


class ButtonGetLevel(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, number):
        super().__init__(all_sprites)
        pg.font.init()
        self.flag = None
        with open('levels.txt') as txt:
            if str(number) in txt.read().split():
                self.color = (255, 255, 255)
                self.flag = True
            else:
                self.flag = False
                self.color = (255, 0, 0)
        surf = pg.Surface((50, 50))
        surf.fill((0, 198, 255))
        pg.draw.circle(surf, self.color, (25, 25), 25)
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

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height and self.flag:
            self.image = self.final_image
            self.check()
        elif args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 3 \
                and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.check(mode='statistics')

    def check(self, mode='play'):
        self.menu_close_open = (True, mode, self.level)


class ButtonGetStartMenu(Button):
    def __init__(self, pos_x, pos_y, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y, 'textures/btn_menu_start.png', 'textures/btn_menu_final.png',
                         (all_sprites,))
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def check(self):
        self.menu_close_open = (True, 'initial_menu')


class ButtonGetLevelMenu(Button):
    def __init__(self, pos_x, pos_y, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y, 'textures/btn_lvls_start.png',
                         'textures/btn_lvls_final.png', (all_sprites,))
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def check(self):
        self.menu_close_open = (True, 'btn_get_lvl_menu')


class ButtonGetSkins(Button):
    def __init__(self, pos_x, pos_y, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y,
                         'textures/btn_hero_start.png',
                         'textures/btn_hero_final.png',
                         (all_sprites,))
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y


class ButtonRestart(Button):
    def __init__(self, pos_x, pos_y, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y,
                         'textures/btn_restart_start.png',
                         'textures/btn_restart_final.png',
                         (all_sprites,))
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def check(self):
        self.menu_close_open = (True, 'btn_restart')


class ButtonYourAccount(Button):
    def __init__(self, pos_x, pos_y, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y,
                         'textures/account_add.png',
                         'textures/account_add.png',
                         (all_sprites,))
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def check(self):
        self.menu_close_open = (True, 'btn_account')


class ButtonAccount(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, id, name, groups):
        super().__init__(groups)
        surf = pg.Surface((100, 50))
        self.id = id
        self.name = name
        pg.font.init()
        pg.draw.rect(surf, (255, 255, 255), (0, 0, 100, 50))
        font = pg.font.SysFont('arial', 16)
        text = font.render(f'{self.name}', 1, (7, 85, 30))
        surf.blit(text, (int((50 - text.get_width()) / 2), 15))
        self.image = surf
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class ButtonCreateNewAccount(Button, Account):
    def __init__(self, pos_x, pos_y, name, groups):
        Button.__init__(self, pos_x, pos_y,
                        'textures/create_account.png',
                        'textures/create_account.png',
                        groups)
        Account.__init__(self)
        self.name = name

    def run(self):
        try:
            self.create_new_account(self.name)
        except sqlite3.OperationalError:
            print('Аккаунт не был создан')