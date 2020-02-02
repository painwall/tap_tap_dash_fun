import pygame as pg


class Label(pg.sprite.Sprite):
    def __init__(self, groups, coords, size,
                 background=None, image=None,
                 text=None, padding=(0, 0),
                 color_text='black', font='arial',
                 size_font=12):
        super().__init__(groups)
        pg.font.init()
        self.font = pg.font.SysFont(font, size_font)
        self.text = text.split('\n')
        self.padding = padding
        self.size_font = size_font * 1.338307
        if type(color_text) == str:
            self.color_text = pg.Color(color_text)
        elif type(color_text) == tuple:
            self.color_text = color_text
        self.image_label = image
        if type(background) == str:
            self.background = pg.Color(background)
        elif type(background) == tuple:
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
        for ind_row in range(len(self.text)):
            self.image.blit(self.font.render(self.text[ind_row], 1, self.color_text),
                            (self.padding[0], (ind_row + self.padding[1]) * self.size_font))

    def render_image(self):
        self.image = self.image_label
