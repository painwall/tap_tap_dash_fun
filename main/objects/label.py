import pygame as pg


class Label(pg.sprite.Sprite):
    def __init__(self, groups, coords, size, background=None, image=None, text=None, padding=(0, 0), color_text='black', font='arial', size_font=12):
        super().__init__(groups)
        pg.font.init()
        self.font = pg.font.SysFont(font, size_font)
        self.text = text
        self.padding = padding
        self.color_text = pg.Color(color_text)
        self.image_label = image
        self.background = background
        self.image = pg.Surface(size)
        if image:
            self.render_image()
        elif text:
            self.render_text()
        self.rect = self.image.get_rect().move(coords)

    def render_text(self):
        if self.background:
            self.image.fill(self.background)
        self.image.blit(self.font.render(self.text, 1, self.color_text), self.padding)

    def render_image(self):
        self.image = self.image_label
