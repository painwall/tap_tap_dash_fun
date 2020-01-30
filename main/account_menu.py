import pygame as pg
from main.window import clock, screen
from main.objects.group_sprites import all_sprites
from main.delete_all_sprites import delete_all_sprites


class AccountMenu:
    def __init__(self):
        delete_all_sprites()
        self.run()

    def run(self):
        screen.fill((0, 198, 255))
        running = True
        while running:
            screen.fill((0, 198, 255))
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

            pg.display.flip()
