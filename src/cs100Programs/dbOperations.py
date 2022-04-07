import sqlite3

names = []
mothers = {}
fathers = {}

def openDB():
    global mothers, fathers
    connection = sqlite3.connect('db')
    cursor = connection.cursor()
    cursor.execute('select * from personsName')
    for name in cursor:
        names.append(name[0])
		
    cursor.execute('select * from personsMother')
    for row in cursor:
        mothers[row[0]] = row[1]

    cursor.execute('select * from personsFather')
    for row in cursor:
        fathers[row[0]] = row[1]
	
    connection.close()
	
def closeDB():
    global mothers, fathers
    connection = sqlite3.connect('db')
    cursor = connection.cursor()

    cursor.execute('delete from personsName')
    cursor.execute('delete from personsMother')
    cursor.execute('delete from personsFather')

    for name in names:
        operation = "insert into personsName values ('" + name + "')"
        cursor.execute(operation)

    for child, mother in mothers.iteritems():
        operation = "insert into personsMother values('" + child + "', '" + mother + "')"
        cursor.execute(operation)

    for child, father in fathers.iteritems():
        operation = "insert into personsFather values('" + child + "', '" + father + "')"
        cursor.execute(operation)

    connection.commit()
    connection.close()
