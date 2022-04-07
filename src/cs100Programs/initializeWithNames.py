import sqlite3

names = ("Woodfield, Scott", "Woodfield, Norman Ray", "Croom, Florance Clementina", "Woodfield, Ray Weldon", "Campbell, Vera Jane",
         "Croom, Martin Herman", "Shingleton, Hazel Catherine", "Woodfield, John Aaron", "Chadwick, Maragaret May", "Campbell, Warren",
         "White, Mary Eliza", "Croom, Major Hawley", "Ward, Ada Florence", "Shingleton, Richard Thomas", "Ketchum, Clementina",)

names = sorted(names)

connection = sqlite3.connect('db')
cursor = connection.cursor()
cursor.execute("delete from personsName")
cursor.execute("delete from personsMother")
cursor.execute("delete from personsFather")
for name in names:
     operation = "insert into personsName values ('" + name + "')"
     cursor.execute(operation)
connection.commit()
connection.close()
