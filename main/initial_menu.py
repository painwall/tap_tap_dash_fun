import pygame as pg
from main.window import all_sprites, clock, screen
from main.objects.buttons import ButtonGetLevelMenu, ButtonGetSkins
from main.delete_all_sprites import delete_all_sprites


class InitialMenu:
    def __init__(self):
        delete_all_sprites()
        self.btn_get_lvl_menu = \
            ButtonGetLevelMenu(300, 275)
        self.btn_get_skins = \
            ButtonGetSkins(350, 325)

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
            if self.btn_get_lvl_menu.menu_close_open[0] == True:
                menu_close_open = self.btn_get_lvl_menu.menu_close_open
                running = False

        try:
            from main.level_menu import LevelMenu
            LevelMenu()

        except IndexError:
            print('ошибка')
