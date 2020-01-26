import pygame as pg
from main.objects.group_sprites import all_sprites


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


class ButtonGetStartMenu(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = pg.image.load('textures/btn_menu_start.png')
        self.final_image = pg.image.load('textures/btn_menu_final.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.menu_close_open = (False,)
        self.speed = 20

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]

        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
            self.check()
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 4:
            self.rect.x += self.speed
        elif args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 5:
            self.rect.x -= self.speed

    def check(self):
        self.menu_close_open = (True, 'initial_menu')


class ButtonGetLevelMenu(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pg.image.load('textures/btn_lvls_start.png')
        self.final_image = pg.image.load('textures/btn_lvls_final.png')
        self.menu_close_open = ('False',)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 15

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if args[0] and args[0].type == pg.MOUSEBUTTONDOWN:
            if args[0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                    and self.rect.y <= y <= self.rect.y + self.rect.height:
                self.image = self.final_image
                self.check()
            elif args[0].button == 5:
                self.move(self.speed)
            elif args[0].button == 4:
                self.move(-self.speed)

    def check(self):
        self.menu_close_open = (True, 'btn_get_lvl_menu')

    def move(self, speed):
        self.rect.y += speed


class ButtonGetSkins(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pg.image.load('textures/btn_hero_start.png')
        self.final_image = pg.image.load('textures/btn_hero_final.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
        self.menu_close_open = (False,)
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.image = self.final_image
            self.check()

    def check(self):
        self.menu_close_open = (True, 'btn_restart')
