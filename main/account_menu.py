import pygame as pg
from main.window import clock, screen
from main.objects.group_sprites import all_sprites
from main.delete_all_sprites import delete_all_sprites
from main.objects.account import Account
from main.objects.buttons import ButtonAccount, ButtonCreateNewAccount
from main.objects.input_field import InputField
from main.objects.group_sprites import all_sprites, accounts_group

class AccountMenu:
    def __init__(self):
        delete_all_sprites()
        self.number = 200
        self.account = Account()
        self.update_accounts()
        self.input_field = InputField(0, 0, (all_sprites,))
        self.btn_create_new_account = ButtonCreateNewAccount(0, 60, self.input_field.text, (all_sprites, ))
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
                accounts_group.update(event)
                self.update_accounts()
                self.btn_create_new_account.name = self.input_field.text
            all_sprites.draw(screen)
            accounts_group.draw(screen)
            pg.display.flip()

    def update_accounts(self):
        delete_all_sprites(groups=(accounts_group,))
        for ind in range(len(self.account.get_list_accounts())):
            ButtonAccount(0, ind * 60 + self.number, self.account.list_accounts[ind][0], self.account.list_accounts[ind][1], accounts_group)