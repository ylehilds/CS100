#!/usr/bin/env python
import os , sys
import cgi
import cgitb
import sqlite3
cgitb.enable()

variables ={"%newName%":"","%errorMessageArea%":"","%listOfPeople%":"","%child%":"","%mother%":"","%father%":"","%root%":"","%f%":"","%m%":"","%ff%":"","%fm%":"","%mf%":"","%mm%":"","%fff%":"","%ffm%":"","%fmf%":"","%fmm%":"","%mff%":"","%mfm%":"","%mmf%":"","%mmm%":""}
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

    cursor.execute('select * from personsFather')
    for row in cursor:
        fathers[row[0]] = row[1]

    connection.close()

def addPerson(form):
    #cgi.test()
    #print "Lehi"
    global names
    if form.has_key("newName") and len(form["newName"].value) > 0:
        name = form["newName"].value
        if not (name in names):
            names.append(name)

def deleteSelectedPerson(form):
    global names, mothers, fathers
    if form.has_key("listOfPeople"):
        person = form["listOfPeople"].value
        if person in names:
            names.remove(person)
        if person in mothers:
            del mothers[person]
            deletePersonAsParent(person, mothers)        
        if person in fathers:
            del fathers[person]
            deletePersonAsParent(person, fathers)
            
           



def deletePersonAsParent(parent, parents):
    childrenToDelete = []
    for child in parents:
        if parents[child] == parent:
            childrenToDelete.append(child)
    for child in childrenToDelete:
        del parents[child]


def addParents(form):
    global names
    if form.has_key("child"):
        child = form["child"].value
        if child in names:
            addParent(form, child, "mother") 
            addParent(form, child, "father")   
   

def addParent(form, child, parentsType):
    global names, mothers, fathers
    if form.has_key(parentsType):
        parent = form[parentsType].value
        if parent in names:
            if parentsType == "mother":
                mothers[child] = parent
            elif parentsType == "father":
                fathers[child] = parent
            


def ShowPedigreeChart(form):
    global variables, mothers, fathers 
    if form.has_key("listOfPeople"):
        name = form["listOfPeople"].value
        variables["%root%"] = name
        setAllAncestors(name,1,"") 


def setAllAncestors(child, generation, ancestorDesignator):
    if generation <=3:
        setAncestor(child, "m", generation, ancestorDesignator)
        setAncestor(child, "f", generation, ancestorDesignator)
        
def setAncestor(child, gender, generation, ancestorDesignator):
    global variables, mothers, fathers 
    parents = mothers
    if gender=="f":
        parents = fathers
    if child in parents:
        parent = parents[child]
        nextAncestorDesignator =  ancestorDesignator+""+gender
        variables['%' + nextAncestorDesignator + '%'] = parent
        setAllAncestors(parent, generation +1, nextAncestorDesignator)
            

 

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


def processForm():
    global variables, names, mothers, fathers
    form = cgi.FieldStorage()
    if form.has_key("deleteSelectedPerson"):  
        deleteSelectedPerson(form)
    if form.has_key("addPerson"):
        addPerson(form)
        names = sorted(names)
    if form.has_key("addParents"):
        addParents(form)
    if form.has_key("ShowPedigreeChart"):
        ShowPedigreeChart(form)
    variables['%listOfPeople%'] = createListOfPeople(names)
    	  	
    


#Main Method
openDB()
processForm()
print generateHTMLPage(variables)
closeDB()