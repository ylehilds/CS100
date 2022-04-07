import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

#-----------------------------------------------------------------------------
#Create the studentlist table and initialize it
#-----------------------------------------------------------------------------
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


#-----------------------------------------------------------------------------
#Create the grades table and initialize it
#-----------------------------------------------------------------------------
cursor.execute(
    '''create table grades(Id integer primary key,
                           Exam1 integer,
                           Exam2 integer,
                           Final integer,
                           Proj1 integer,
                           Proj2 integer,
                           Proj3 integer,
                           HW1   integer,
                           HW2   integer
                          )
    ''')

gradeValues= [(107756, 87, 91, 89, 99, 100, 95, 88, 73),
              (273411, 97, 99, 94, 75,  77, 62, 21, 30),
              (408827, 72, 77, 68, 110, 110, 110, 100, 100),
              (733101, 95, 72, 81, 91, 92, 70, 88, 81),
              (121051, 81, 74, 71, 72, 81, 77, 74, 75)
             ]

template = 'insert into grades values(?, ?, ?, ?, ?, ?, ?, ?, ?);'
for rowValues in gradeValues:
    connection.execute(template, rowValues)

connection.commit()
connection.close()
