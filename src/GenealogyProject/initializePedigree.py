import sqlite3

names = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",)

names = sorted(names)

connection = sqlite3.connect('db')
cursor = connection.cursor()
cursor.execute("delete from personsName")
cursor.execute("delete from personsMother")
cursor.execute("delete from personsFather")
for name in names:
     operation = "insert into personsName values ('" + name + "')"
     cursor.execute(operation)
cursor.execute("insert into personsFather values('A', 'B');")
cursor.execute("insert into personsMother values('A', 'C');")
cursor.execute("insert into personsFather values('B', 'D');")
cursor.execute("insert into personsMother values('B', 'E');")
cursor.execute("insert into personsFather values('C', 'F');")
cursor.execute("insert into personsMother values('C', 'G');")
cursor.execute("insert into personsFather values('D', 'H');")
cursor.execute("insert into personsMother values('D', 'I');")
cursor.execute("insert into personsFather values('E', 'J');")
cursor.execute("insert into personsMother values('E', 'K');")
cursor.execute("insert into personsFather values('F', 'L');")
cursor.execute("insert into personsMother values('F', 'M');")
cursor.execute("insert into personsFather values('G', 'N');")
cursor.execute("insert into personsMother values('G', 'O');")
connection.commit()
connection.close()
