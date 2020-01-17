from main.window import WIN_HEIGHT, WIN_WIDTH


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
