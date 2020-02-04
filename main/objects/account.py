import sqlite3


class Account:
    def __init__(self, id_account, name=None):
        self.con = sqlite3.connect('data/accounts/accounts.db')
        self.cur = self.con.cursor()
        self.get_list_accounts()
        self.id = id_account
        self.name = name

    def log_in(self):
        with open('data/accounts/id_account.txt', mode='w') as txt:
            txt.write(str(self.id))

    def return_log_in_account(self):
        with open('data/accounts/id_account.txt') as txt:
            return int(txt.read())

    def delete_account(self):
        self.cur.execute(f'DELETE FROM accounts WHERE id = {self.id}')
        self.con.commit()
        with open('data/accounts/id_account.txt', mode='w') as txt:
            txt.write('0')

    def edit_name(self):
        pass

    def get_list_accounts(self):
        list_accounts = self.cur.execute('SELECT * FROM accounts').fetchall()
        return list_accounts

    def create_new_account(self, name):
        self.cur.execute(f'INSERT INTO accounts (account_name, pass_levels) VALUES ("{name}", "0 1")')
        self.con.commit()