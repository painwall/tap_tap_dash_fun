import pygame as pg
from main.window import screen, clock
from main.objects.group_sprites import all_sprites
from main.objects.buttons import ButtonGetLevelMenu, ButtonRestart
from main.delete_all_sprites import delete_all_sprites
from main.objects.label import Label


class RestartMenu:
    def __init__(self, level):
        self.level = level
        delete_all_sprites()
        self.btn_get_lvl_menu = ButtonGetLevelMenu(300, 275, (all_sprites,))
        self.btn_restart = ButtonRestart(300, 375, (all_sprites,))
        self.labels = {
            'help_restart': Label(all_sprites, (550, 580), (220, 25),
                                  background='white',
                                  text='R - перезапуск уровня в этом меню',
                                  size_font=16),
            'help_play': Label(all_sprites, (30, 30), (235, 70),
                               text='Управление:\n1. Стрелочки для смены направления движения\n'
                                    '2. Пробел - прыжок', background='white', size_font=16)
        }
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
                if event.type == pg.KEYDOWN and event.key == 114:
                    running = False
                    event = (0, 'btn_restart')


            if self.btn_get_lvl_menu.event[0]:
                event = self.btn_get_lvl_menu.event
                running = False
            elif self.btn_restart.event[0]:
                event = self.btn_restart.event
                running = False

            all_sprites.draw(screen)
            pg.display.flip()

        if event[1] == 'btn_get_lvl_menu':
            from main.level_menu import LevelMenu
            LevelMenu()
        elif event[1] == 'btn_restart':
            from main.playing import Play
            Play(self.level)
