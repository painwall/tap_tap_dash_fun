WIN_WIDTH = 800
WIN_HEIGHT = 600


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIN_WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - WIN_HEIGHT // 2)


class Cursor:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        try:
            obj.end_coord_x += self.dx
        except BaseException:
            pass
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIN_WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - WIN_HEIGHT // 2 - 75)
