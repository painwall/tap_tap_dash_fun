import sqlite3


class Account:
    def __init__(self, id):
        self.id = id

    def log_in(self, id):
        with open('data/accounts/accounts.db', mode='w') as txt:
            txt.write(str(id))
        self.id = id

    def delete_account(self):
        pass

    def edit_name(self):
        pass
