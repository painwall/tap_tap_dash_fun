import pygame as pg

sc = pg.display.set_mode((300, 300))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        print(event)


