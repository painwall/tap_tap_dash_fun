import pygame as pg
from main.window import clock, screen
from main.objects.group_sprites import all_sprites
from main.delete_all_sprites import delete_all_sprites
from main.objects.account import Account
from main.objects.buttons import ButtonAccount
from main.objects.input_field import InputField

class AccountMenu:
    def __init__(self):
        delete_all_sprites()
        self.number = 200
        with open('data/accounts/id_account.txt') as txt:
            self.account = Account(int(txt.read()))
        for ind in range(len(self.account.list_accounts)):
            print(0, ind * 60 + self.number, self.account.list_accounts[ind][0], self.account.list_accounts[ind][1])
            ButtonAccount(0, ind * 60 + self.number, self.account.list_accounts[ind][0], self.account.list_accounts[ind][1])
        self.input_field = InputField(0, 0)
        self.run()

    def run(self):
        screen.fill((0, 198, 255))
        running = True
        while running:
            screen.fill((0, 198, 255))
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                all_sprites.update(event)
            all_sprites.draw(screen)
            pg.display.flip()
