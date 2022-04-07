import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

cursor.execute(
    '''insert into studentlist values(107756, "Mouse, Mickey");''');

connection.commit()
connection.close()
