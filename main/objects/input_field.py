import pygame as pg
from main.objects.group_sprites import all_sprites


class InputField(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, groups, font_size=16):
        super().__init__(groups)
        pg.font.init()
        self.font = pg.font.SysFont('arial', font_size)
        self.text = ''
        self.surf = pg.Surface((width, height))
        self.rect = self.surf.get_rect().move(pos_x, pos_y)
        self.surf.fill((255, 255, 255))
        self.image = self.surf

    def update(self, *args):
        if args and args[0].type == pg.KEYDOWN:
            if args[0].key == 8:
                self.text = self.text[:-1]
            else:
                self.text += str(args[0].unicode)
            self.render_text()

    def render_text(self):
        self.surf.fill((255, 255, 255))
        text = self.font.render(f'{self.text}', 1, (7, 85, 30))
        self.surf.blit(text, ((self.rect.width - text.get_width()) // 2, (self.rect.height - text.get_height()) // 2))
        self.image = self.surf
