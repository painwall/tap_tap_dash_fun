import pygame as pg
from main.window import clock, screen
from main.delete_all_sprites import delete_all_sprites
from main.objects.account import Account, check_account
from main.objects.buttons import ButtonAccount, ButtonCreateNewAccount, ButtonGetStartMenu
from main.objects.input_field import InputField
from main.objects.group_sprites import all_sprites, accounts_group, offset_y_group
from main.objects.scrollbar import Scrollbar
from main.objects.label import Label
from main.objects.buttons import ButtonDeleteAccount


class AccountMenu:
    def __init__(self):
        delete_all_sprites()
        self.number = 240
        self.account = Account(None)
        self.input_field = InputField(250, 40, 300, 50, (offset_y_group, all_sprites), 18)
        self.btn_create_new_account = \
            ButtonCreateNewAccount(350, 150, self.input_field.text, (all_sprites, offset_y_group), None)
        self.scrollbar = Scrollbar(790, 0, (offset_y_group,), offset_y=True)
        self.btn_get_start_menu = ButtonGetStartMenu(20, 550, (all_sprites,))
        self.labels = {'field_new_account': Label((all_sprites, offset_y_group), (307.5, 10), (185, 20),
                                                  text='Поле для ввода имени аккаунта:', background=(0, 198, 255),
                                                  size_font=14),
                       'label_status_new_account': Label((all_sprites, offset_y_group),
                                                         (300, 100), (200, 50), text=' ', background=(0, 198, 255),
                                                         size_font=14)
                       }
        self.list_btns_account = []
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
                self.labels['label_status_new_account'].text = check_account(self.input_field.text)[0].split('\n')
                self.labels['label_status_new_account'].render_text()
                self.btn_create_new_account.name = self.input_field.text

            for btn_account in self.list_btns_account:
                btn_account[0].image_button()
                if btn_account[0].event[0]:
                    if btn_account[0].event[1] == 'log_in':
                        btn_account[0].log_in()
                        btn_account[0].event = (False,)
                elif btn_account[1].event[0]:
                    if btn_account[1].event[1] == 'delete_account':
                        btn_account[1].event = (False,)
                        self.update_accounts()
            if self.btn_create_new_account.event[0]:
                self.update_accounts()
                self.btn_create_new_account.event = (False,)
            if self.btn_get_start_menu.event[0]:
                event = self.btn_get_start_menu.event
                running = False

            all_sprites.draw(screen)
            pg.display.flip()

        if event[1] == 'initial_menu':
            from main.initial_menu import InitialMenu
            InitialMenu()

    def update_accounts(self):
        delete_all_sprites(groups=(accounts_group,))
        self.list_btns_account = [
            (
                ButtonAccount(250, ind * 64 + self.number, self.account.get_list_accounts()[ind][0],
                              self.account.get_list_accounts()[ind][1], (accounts_group, offset_y_group,
                                                                         all_sprites)),
                ButtonDeleteAccount(570, ind * 64 + self.number, self.account.get_list_accounts()[ind][0],
                                    (accounts_group, offset_y_group, all_sprites))
            ) for ind in range(len(self.account.get_list_accounts()))]
