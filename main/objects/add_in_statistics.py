import sqlite3


def add_in_statistics(table, columns, values):
    con_stat = sqlite3.connect('data/statistics.db')
    cur_stat = con_stat.cursor()
    cur_stat.execute(f'INSERT INTO {table} {columns} values{values}')
    con_stat.commit()
