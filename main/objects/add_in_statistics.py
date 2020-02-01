import sqlite3


def add_in_statistics(table, columns, values, id_ac=True):
    # table = <название таблицы>
    # columns = <(название колонки в таблице, ...)>
    # values = <(значение, ...)>
    with open('data/accounts/id_account.txt') as txt:
        id_account = int(txt.read())
    con_stat = sqlite3.connect('data/statistics.db')
    cur_stat = con_stat.cursor()
    if id_ac:
        columns = list(columns)
        columns.append('id_account')
        columns = tuple(columns)
        values = list(values)
        values.append(id_account)
        values = tuple(values)
        cur_stat.execute(f'INSERT INTO {table} {columns} values{values}')
    else:
        cur_stat.execute(f'INSERT INTO {table} {columns} values{values}')
    con_stat.commit()


def add_pass_level(level):
    con = sqlite3.connect('data/statistics.db')
    cur = con.cursor()
    with open('data/accounts/id_account.txt') as txt:
        id_account = int(txt.read())
    pass_levels = cur.execute(f'SELECT pass_levels FROM accounts WHERE id={id_account}').fetchall()[0].split(' ')
    if str(level + 1) not in pass_levels:
        pass_levels += f' {level + 1}'
