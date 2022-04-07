#!/usr/bin/env python

import cgi, cgitb
cgitb.enable()

def celsiusToFahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5.0 + 32.0
    result = round(fahrenheit, 0)
    return result

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32.0) * 5.0 / 9.0
    result = round(celsius, 0)
    return result

result = "Content-type: text/html\n\n"

celsiusValue = ""
fahrenheitValue = ""

form = cgi.FieldStorage()

if form.has_key("celsius") and len(form["celsius"].value) > 0:
    try:
        celsius = float(form["celsius"].value)
        fahrenheit = celsiusToFahrenheit(celsius)
        fahrenheitValue = str(fahrenheit)
    except:
        celsiusValue = "ERROR: You must enter an integer"

if form.has_key("fahrenheit") and len(form["fahrenheit"].value) > 0:
    try:
        fahrenheit = float(form["fahrenheit"].value)
        celsius = fahrenheitToCelsius(fahrenheit)
        celsiusValue = str(celsius)
    except:
        fahrenheitValue = "ERROR: You must enter an integer"

source = open("convertExample/Convert.html")
result += source.read()
result = result.replace("%celsius%", celsiusValue)
result = result.replace("%fahrenheit%", fahrenheitValue)

print result 