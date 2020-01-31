import sqlite3


class Account:
    def __init__(self, id):
        self.id = id
        self.con = sqlite3.connect('data/accounts/accounts.db')
        self.cur = self.con.cursor()
        self.get_list_accounts()

    def log_in(self, id):
        with open('data/accounts/accounts.db', mode='w') as txt:
            txt.write(str(id))
        self.id = id

    def delete_account(self):
        pass

    def edit_name(self):
        pass

    def get_list_accounts(self):
        self.list_accounts = self.cur.execute('SELECT * FROM accounts').fetchall()

    def create_new_account(self, name):
        self.cur.execute(f'INSERT INTO accounts (name) values({name})')
