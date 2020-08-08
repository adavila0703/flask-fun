import sqlite3

connection = sqlite3.connect('cool.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'

cursor.execute(create_table)

#adding single user to DB
user = (1, 'bob', 'pass1')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'

cursor.execute(insert_query, user)

#adding many users to db
users = [
    (2, 'test', 'pass'),
    (3, 'hello', 'pass2')
]

cursor.executemany(insert_query, users)


#get data in *, you can specify which column
select_query = 'SELECT * FROM users'
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
