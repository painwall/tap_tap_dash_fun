import pygame as pg


class CheckBox(pg.sprite.Sprite):
    def __init__(self, coords, groups, size=(64, 64)):
        super().__init__(groups)
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect().move(coords)
        self.mark = pg.image.load('textures/mark.png')
        self.flag = False
        self.color = pg.Color('white')
        self.event = (False,)
        self.image.fill(self.color)

    def edit_image(self):
        if self.flag:
            self.flag = False
            self.image.fill(self.color)
            # pg.draw.rect(self.image, (0, 0, 0), (10, 10, 10, 10))
            self.image.blit(self.mark, (0, 0))
        else:
            self.flag = True
            self.image.fill(self.color)

    def update(self, *args):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]

        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[
            0].button == 1 and self.rect.x <= x <= self.rect.x + self.rect.width \
                and self.rect.y <= y <= self.rect.y + self.rect.height:
            self.edit_image()
            self.make_event()

    def make_event(self):
        self.event = (True, 'check_box')
