import sqlite3

names = ("Alcantara, Lehi", "Alcantara, Edilson Ray", "Ribeiro, Ana Cleide", "Alcantara, Alexandro", "Ribeiro, Ianna Jane",
         "Ribeiro, Luz", "Vianna, Norma Catarina", "Alcantara, Joao Arao", "Silva, Marcos May", "Souza, Luciano",
         "Menedes, Maria Elizabete", "Alcantara, Victor clementino", "Costa, Adao florentino", "Silva, Ricardo Thomas", "Mendes, Jacqueline",)

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
