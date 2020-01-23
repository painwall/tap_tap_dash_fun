from PIL import Image
import pygame as pg
from main.objects.tiles import Tile, MoveUpTile, MoveDownTile, MoveLeftTile, MoveRightTile, JumpTile, FinishTile
from main.window import screen, clock
from main.objects.group_sprites import all_sprites
from main.objects.camera import Camera
from main.objects.skin import skin_group
from main.objects.player import player_group
from main.delete_all_sprites import delete_all_sprites
from main.objects.player import Player
from main.objects.timer import Timer
from main.objects.group_sprites import clock_group
import os

PLAYER = (237, 28, 36, 255)
RIGHT_TILE = (0, 162, 232, 255)
LEFT_TILE = (34, 177, 76, 255)
UP_TILE = (255, 127, 39, 255)
DOWN_TILE = (255, 242, 0, 255)
TILE = (0, 0, 0, 255)
JUMP_TILE = (63, 72, 204, 255)
FINISH_TILE = (163, 73, 164, 255)
UP_JUMP_TILE = (255, 201, 14, 255)
DOWN_JUMP_TILE = (239, 228, 176, 255)
LEFT_JUMP_TILE = (181, 230, 29, 255)
RIGHT_JUMP_TILE = (153, 217, 234, 255)

class Play:
    def __init__(self, level):
        self.camera = Camera()
        self.timer = Timer(50, 50)
        self.level = level
        self.generate_level()

    def generate_level(self):
        delete_all_sprites()
        image = Image.open(f'levels/{self.level}/level.png')
        width = image.size[0]
        height = image.size[1]

        for y in range(width):
            for x in range(height):
                if image.getpixel((y, x)) == TILE:
                    Tile(y, x)
                if image.getpixel((y, x)) == PLAYER:
                    Tile(y, x)
                    self.player = Player(y, x, float(open(f'levels/{self.level}/speed.txt', encoding='ANSI').read()))
                elif image.getpixel((y, x)) == UP_TILE:
                    Tile(y, x)
                    MoveUpTile(y, x)
                elif image.getpixel((y, x)) == DOWN_TILE:
                    Tile(y, x)
                    MoveDownTile(y, x)
                elif image.getpixel((y, x)) == LEFT_TILE:
                    Tile(y, x)
                    MoveLeftTile(y, x)
                elif image.getpixel((y, x)) == RIGHT_TILE:
                    Tile(y, x)
                    MoveRightTile(y, x)
                elif image.getpixel((y, x)) == JUMP_TILE:
                    Tile(y, x)
                    JumpTile(y, x)
                elif image.getpixel((y, x)) == RIGHT_JUMP_TILE:
                    Tile(y, x)
                    JumpTile(y, x)
                    MoveRightTile(y, x)
                elif image.getpixel((y, x)) == LEFT_JUMP_TILE:
                    Tile(y, x)
                    JumpTile(y, x)
                    MoveLeftTile(y, x)
                elif image.getpixel((y, x)) == DOWN_JUMP_TILE:
                    Tile(y, x)
                    JumpTile(y, x)
                    MoveDownTile(y, x)
                elif image.getpixel((y, x)) == UP_JUMP_TILE:
                    Tile(y, x)
                    JumpTile(y, x)
                    MoveUpTile(y, x)
                elif image.getpixel((y, x)) == FINISH_TILE:
                    FinishTile(y, x)
        self.play()

    def play(self):
        running = True
        while running:
            screen.fill((0, 198, 255))
            for event in pg.event.get():
                player_group.update(event)

            self.player.move()
            self.player.skin.move(self.player.rect.x, self.player.rect.x)
            self.camera.update(self.player)
            for sprite in all_sprites:
                self.camera.apply(sprite)
            self.player.skin.update(pg.time.get_ticks())
            all_sprites.draw(screen)
            clock_group.update()
            clock_group.draw(screen)
            skin_group.draw(screen)
            pg.display.flip()
            clock.tick(120)
            if self.player.menu_close_open[0] == True:
                menu_close_open = self.player.menu_close_open
                running = False

        if menu_close_open[1] == 'restart_menu':
            from main.restart_menu import RestartMenu
            RestartMenu(self.level)
        elif menu_close_open[1] == 'new_level':
            if int(self.level) >= len(os.listdir('levels')):
                from main.level_menu import LevelMenu
                LevelMenu()
            else:
                with open('levels.txt', mode='a', encoding='ANSI') as txt:
                    txt.write(f' {self.level + 1}')
                Play(self.level + 1)