import pygame as pg
from main.objects.account import Account, check_account
from main.objects.label import Label
import sqlite3


class Button(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, final_image, groups):
        super().__init__(groups)
        self.image = pg.image.load(image)
        self.final_image = pg.image.load(final_image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.event = (False,)
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
            self.run()
            self.make_event()
        if self.move and args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 4:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        elif self.move and args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 5:
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y

    def make_event(self):
        pass

    def run(self):
        pass


class ButtonGetLevel(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, number, groups):
        super().__init__(groups)
        pg.font.init()
        self.con = sqlite3.connect('data/accounts/accounts.db')
        self.cur = self.con.cursor()
        self.flag = None
        with open('data/accounts/id_account.txt') as txt:
            id_account = int(txt.read())
            print(self.cur.execute(f'SELECT pass_levels'
                                   f' FROM accounts WHERE id={id_account}').fetchall())
            if str(number) \
                    in self.cur.execute(f'SELECT pass_levels'
                                        f' FROM accounts WHERE id={id_account}').fetchall()[0][0].split(' '):
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
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.event = (False,)

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height and self.flag:
            self.image = self.final_image
            self.make_event()
        elif args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 3 \
                and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.make_event(mode='statistics')

    def make_event(self, mode='play'):
        self.event = (True, mode, self.level)


class ButtonGetStartMenu(Button):
    def __init__(self, pos_x, pos_y, groups, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y, 'textures/btn_menu_start.png', 'textures/btn_menu_final.png',
                         groups)
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def make_event(self):
        self.event = (True, 'initial_menu')


class ButtonGetLevelMenu(Button):
    def __init__(self, pos_x, pos_y, groups, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y, 'textures/btn_lvls_start.png',
                         'textures/btn_lvls_final.png', groups)
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def make_event(self):
        self.event = (True, 'btn_get_lvl_menu')


class ButtonGetSkins(Button):
    def __init__(self, pos_x, pos_y, groups, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y,
                         'textures/btn_hero_start.png',
                         'textures/btn_hero_final.png',
                         groups)
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y


class ButtonRestart(Button):
    def __init__(self, pos_x, pos_y, groups, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y,
                         'textures/btn_restart_start.png',
                         'textures/btn_restart_final.png',
                         groups)
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def make_event(self):
        self.event = (True, 'btn_restart')


class ButtonYourAccount(Button):
    def __init__(self, pos_x, pos_y, groups, move=False, speed_x=0, speed_y=0):
        super().__init__(pos_x, pos_y,
                         'textures/account_add.png',
                         'textures/account_add.png',
                         groups)
        self.move = move
        self.speed_x = speed_x
        self.speed_y = speed_y

    def make_event(self):
        self.event = (True, 'btn_account')


class ButtonAccount(pg.sprite.Sprite, Account):
    def __init__(self, pos_x, pos_y, id_account, name_account, groups):
        pg.sprite.Sprite.__init__(self, groups)
        Account.__init__(self, id_account=id_account, name=name_account)
        pg.font.init()
        surf = pg.Surface((300, 64))
        surf.fill((255, 255, 255))
        self.image = surf
        self.font = pg.font.SysFont('arial', 20)
        self.image_button()
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.event = (False,)

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]

        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.make_event()

    def make_event(self):
        self.event = (True, 'log_in')
        self.image_button()
        print(f'Вход в аккаунт с id ={self.id}')

    def image_button(self):
        if self.return_log_in_account() == self.id:
            self.image.fill(pg.Color('pink'))
        else:
            self.image.fill(pg.Color('white'))
        self.text = self.font.render(f'{self.name}', 1, (7, 85, 30))
        self.image.blit(self.text, (10, 15))


class ButtonCreateNewAccount(Button, Account):
    def __init__(self, pos_x, pos_y, name, groups, id):
        Button.__init__(self, pos_x, pos_y,
                        'textures/create_account.png',
                        'textures/create_account.png',
                        groups)
        Account.__init__(self, id)
        self.name = name

    def run(self):
        try:
            if check_account(self.name)[-1]:
                self.create_new_account(self.name)
        except sqlite3.OperationalError:
            import traceback
            print(traceback.print_exc())
            print('Аккаунт не был создан')

    def make_event(self):
        self.event = (True, 'create_new_account')


class ButtonDeleteAccount(Button, Account):
    def __init__(self, pos_x, pos_y, id_account, groups):
        Button.__init__(self, pos_x, pos_y,
                        'textures/delete_account.png',
                        'textures/delete_account.png', groups)
        Account.__init__(self, id_account)

    def run(self):
        if self.id > 0:
            self.delete_account()

    def make_event(self):
        self.event = (True, 'delete_account')