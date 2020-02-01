import pygame as pg
from main.window import clock, screen
from main.delete_all_sprites import delete_all_sprites
from main.objects.account import Account
from main.objects.buttons import ButtonAccount, ButtonCreateNewAccount, ButtonGetStartMenu
from main.objects.input_field import InputField
from main.objects.group_sprites import all_sprites, accounts_group, offset_y_group
from main.objects.scrollbar import Scrollbar


class AccountMenu:
    def __init__(self):
        delete_all_sprites()
        self.number = 200
        self.account = Account(None)
        self.input_field = InputField(250, 20, 300, 50, (offset_y_group, all_sprites))
        self.btn_create_new_account = \
            ButtonCreateNewAccount(0, 60, self.input_field.text, (offset_y_group, all_sprites), None)
        self.scrollbar = Scrollbar(790, 0, (offset_y_group,), offset_y=True)
        self.btn_get_start_menu = ButtonGetStartMenu(300, 550, (all_sprites,))
        self.index_btn_account = None
        self.update_accounts()
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
                self.scrollbar.update(event)
                self.btn_create_new_account.name = self.input_field.text

            for btn_account in self.list_btns_account:
                if btn_account.menu_close_open[0]:
                    if btn_account.menu_close_open[1] == 'log_in':
                        btn_account.log_in()
                        btn_account.menu_close_open = (False,)
            if self.btn_create_new_account.menu_close_open[0]:
                self.update_accounts()
            if self.btn_get_start_menu.menu_close_open[0]:
                menu_close_open = self.btn_get_start_menu.menu_close_open
                running = False

            all_sprites.draw(screen)
            accounts_group.draw(screen)
            pg.display.flip()

        if menu_close_open[1] == 'initial_menu':
            from main.initial_menu import InitialMenu
            InitialMenu()

    def update_accounts(self):
        delete_all_sprites(groups=(accounts_group,))
        self.list_btns_account = []
        self.list_btns_account = [
            ButtonAccount(0, ind * 60 + self.number, self.account.get_list_accounts()[ind][0],
                          self.account.get_list_accounts()[ind][1], (accounts_group, offset_y_group,
                                                                     all_sprites))
            for ind in range(len(self.account.get_list_accounts()))]
