import pygame as pg
from main.objects.buttons import ButtonGetLevelMenu

class StatisticsMenu:
    def __init__(self):
        self.btn_get_level_menu = ButtonGetLevelMenu(0, 0)

    def run(self):
        running = True
        while running:
            pass