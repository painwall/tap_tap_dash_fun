import pygame as pg
from main.window import all_sprites, clock, screen
from main.objects.buttons import ButtonGetLevelMenu, ButtonGetSkins
from main.delete_all_sprites import delete_all_sprites
from main.imports import import_lvl_menu


class InitialMenu:
    def __init__(self):
        delete_all_sprites()
        self.btn_get_lvl_menu = \
            ButtonGetLevelMenu('../textures/btn_lvls_start.png', '../textures/btn_lvls_final.png', 300, 275)
        self.btn_get_skins = \
            ButtonGetSkins('../textures/btn_hero_start.png', '../textures/btn_hero_final.png', 350, 325)

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
                if self.btn_get_lvl_menu.menu_close_open[0] == True:
                    menu_close_open = self.btn_get_lvl_menu.menu_close_open
                    running = False
            all_sprites.draw(screen)
            pg.display.flip()

        try:
            if menu_close_open[1] == 'btn_get_lvl_menu':
                import_lvl_menu()

        except IndexError:
            print('ошибка')
