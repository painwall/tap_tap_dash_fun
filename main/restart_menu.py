import pygame as pg
from main.window import screen, clock
from main.objects.group_sprites import all_sprites
from main.objects.buttons import ButtonGetLevelMenu, ButtonRestart
from main.delete_all_sprites import delete_all_sprites


class RestartMenu:
    def __init__(self, level):
        self.level = level
        self.run()

    def run(self):
        delete_all_sprites()
        btn_get_lvl_menu = ButtonGetLevelMenu(300, 275, (all_sprites,))
        btn_restart = ButtonRestart(300, 375, (all_sprites,))
        running = True
        while running:
            screen.fill((0, 198, 255))
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    all_sprites.update(event)
                if event.type == pg.KEYDOWN and event.key == 114:
                    running = False
                    event = (0, 'btn_restart')


            if btn_get_lvl_menu.event[0] == True:
                event = btn_get_lvl_menu.event
                running = False
            elif btn_restart.event[0] == True:
                event = btn_restart.event
                running = False

            all_sprites.draw(screen)
            pg.display.flip()

        if event[1] == 'btn_get_lvl_menu':
            from main.level_menu import LevelMenu
            LevelMenu()
        elif event[1] == 'btn_restart':
            from main.playing import Play
            Play(self.level)
