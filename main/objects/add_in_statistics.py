import sqlite3


def add_in_statistics(table, columns, values):
    con = sqlite3.connect('statistics.db')
    cur = con.cursor()
    cur.execute(f'INSERT INTO {table} {columns} values{values}')
    con.commit()
