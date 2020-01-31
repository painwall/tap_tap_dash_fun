import pygame as pg
from main.objects.group_sprites import all_sprites

class InputField(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        pg.font.init()
        self.font = pg.font.SysFont('arial', 16)
        self.text = ''
        self.surf = pg.Surface((100, 50))
        self.rect = self.surf.get_rect().move(pos_x, pos_y)
        self.surf.fill((255, 255, 255))
        self.image = self.surf

    def update(self, *args):
        if args and args[0].type == pg.KEYDOWN:
            self.text += str(args[0].unicode)
            self.render_text()

    def render_text(self):
        self.surf.fill((255, 255, 255))
        text = self.font.render(f'{self.text}', 1, (7, 85, 30))
        self.surf.blit(text, (0, 0))
        self.image = self.surf