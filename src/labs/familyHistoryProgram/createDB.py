import sqlite3

connection = sqlite3.connect('db')
cursor = connection.cursor()
cursor.execute('''create table personsName (personsName text PRIMARY KEY)''')
cursor.execute('''create table personsMother (personsName text PRIMARY KEY, mothersName text)''')
cursor.execute('''create table personsFather (personsName text PRIMARY KEY, fathersName text)''')
connection.close()
