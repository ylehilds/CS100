import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

cursor.execute(
    '''insert into studentlist values(273411, "Duck, Donald");''');
cursor.execute(
    '''insert into studentlist values(408827, "Pan, Peter");''');
cursor.execute(
    '''insert into studentlist values(733101, "White, Snow");''');
cursor.execute(
    '''insert into studentlist values(121051, "Mouse, Mickey");''');

connection.commit()
connection.close()
