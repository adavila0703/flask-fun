import sqlite3


def maketable():
    connection = sqlite3.connect('userdata.db')

    cursor = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'

    cursor.execute(create_table)

    create_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, itemname text, stock int, price int)'

    cursor.execute(create_table)

    connection.commit()
    connection.close()
