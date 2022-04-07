import sqlite3

connection = sqlite3.connect("gradebook")
cursor = connection.cursor()

cursor.execute("""SELECT name, exam1, exam2, final
                  FROM  studentlist, grades
		  WHERE studentlist.id = grades.id;
               """)
for tuple in cursor:
    average = (tuple[1] + tuple[2])/2
    print "The average exam score for ", tuple[0], " is ", average, \
          " and the final = ", tuple[3] 

connection.commit()
connection.close()
