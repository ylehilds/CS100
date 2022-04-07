import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

cursor.execute("select * from studentlist;")
for tuple in cursor:
    print tuple

connection.commit()
connection.close()
