import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

cursor.execute(
    '''create table studentlist(Id integer primary key, Name text)''')

studentListValues = [(107756, "Mouse, Mickey"),
                     (273411, "Duck, Donald"),
                     (408827, "Pan, Peter"),
                     (733101, "White, Snow"),
                     (121051, "Mouse, Mickey")
                    ]

template = 'insert into studentlist values(?, ?);'
for rowValues in studentListValues:
	connection.execute(template, rowValues)

connection.commit()
connection.close()


