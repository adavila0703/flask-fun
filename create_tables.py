import sqlite3


def maketable():
    connection = sqlite3.connect('userdata.db')

    cursor = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'

    cursor.execute(create_table)

    connection.commit()
    connection.close()
