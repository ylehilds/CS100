#!/usr/bin/env python
import cgi
import cgitb
import sqlite3
cgitb.enable()

variables ={"%newName%":          "",
            "%errorMessageArea%": "",
            "%listOfPeople%":     "",
           }

names=[]
mothers={}
fathers={}

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

    cursor.execute('os.system(select * from personsFather)')
    for row in cursor:
        fathers[row[0]] = row[1]

    connection.close()


def processForm():
    global variables, names, mothers, fathers
    form = cgi.FieldStorage()
    if form.has_key("deleteSelectedPerson"):  
        deleteSelectedPerson(form)
    if form.has_key("addPerson"):
        addPerson(form)
        names = sorted(names)
    variables['%listOfPeople%'] = createListOfPeople(names)	  	
    
def addPerson(form):
    global names
    if form.has_key("newName") and len(form["newName"].value) > 0:
        name = form["newName"].value
    if not (name in names):
        names.append(name)

def deleteSelectedPerson(form):
    global names
    if form.has_key("listOfPeople"):
        person = form["listOfPeople"].value
        if person in names:
            names.remove(person)
        

def createListOfPeople(names):
    result=""
    if len(names)>0:
        result = '<option value="' + names[0] + '" selected>' + names[0] + '</option>'
    for name in names[1:]:
         result = result + '\n                <option value="' + name + '">' + name + '</option>'
    return result

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
	

def generateHTMLPage (variables):
  result = "Content-type: text/html\n\n"
  source = open("MyFamilyHistory.html", "rt")
  result += source.read()
  source.close()
  for keyword in variables:
    result = result.replace(keyword, variables[keyword])
  return result
#print generateHTMLPage()
openDB()
processForm()
print generateHTMLPage(variables)
closeDB()