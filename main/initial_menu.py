import pygame as pg
from main.window import clock, screen
from main.objects.group_sprites import all_sprites
from main.objects.buttons import ButtonGetLevelMenu, ButtonGetSkins, ButtonYourAccount
from main.delete_all_sprites import delete_all_sprites


class InitialMenu:
    def __init__(self):
        delete_all_sprites()
        self.btn_get_lvl_menu = \
            ButtonGetLevelMenu(300, 275, (all_sprites,))
        self.btn_get_skins = \
            ButtonGetSkins(350, 325, (all_sprites,))
        self.button_your_account = ButtonYourAccount(700, 0, (all_sprites,))
        self.run()

    def run(self):
        running = True
        while running:
            screen.fill((0, 198, 255))
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    all_sprites.update(event)

            all_sprites.draw(screen)
            pg.display.flip()
            if self.btn_get_lvl_menu.event[0]:
                event = self.btn_get_lvl_menu.event
                running = False
            elif self.button_your_account.event[0]:
                event = self.button_your_account.event
                running = False

        try:
            if event[1] == 'btn_get_lvl_menu':
                from main.level_menu import LevelMenu
                LevelMenu()
            if event[1] == 'btn_account':
                from main.account_menu import AccountMenu
                AccountMenu()

        except IndexError:
            import traceback
            print('Ошибка:\n', traceback.format_exc())
            print('ошибка')
