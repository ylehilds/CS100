import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

cursor.execute(
    '''create table studentlist(Id integer primary key, Name text)''')

connection.commit()
connection.close()
