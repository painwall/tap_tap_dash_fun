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
        try:
            con = sqlite3.connect('data/statictics.db')
            cur = con.cursor()
            cur.execute(f'DELETE FROM travel WHERE id = {self.id}')
            con.commit()
        except sqlite3.OperationalError:
            pass
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


def check_account(text):
    if len(text) > 15:
        return (f'Максимальная длина имени равна 15\n Вы ввели {len(text)}', False)
    elif len(text) < 1:
        return (f'Минимальная длина имени равна 1\n Вы ввели {len(text)}', False)

    con = sqlite3.connect('data/accounts/accounts.db')
    cur = con.cursor()
    if len(cur.execute(f'SELECT id FROM accounts WHERE account_name = "{text}"').fetchall()) != 0:
        return ('Такое имя уже существует', False)
    return ('Имя подходит', True)
