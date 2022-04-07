def formLetter(gender, lastName, city, eyeColor):
    file = open(getMediaPath("formLetter.txt"), "wt")
    file.write("Dear ")
    if gender == "F" or gender == "f":
        file.write("Ms. " + lastName + ":\n")
    if gender == "M" or gender == "m":
        file.write("Mr. " + lastName + ":\n")
    file.write("I am writing to remind you of the offer ")
    file.write("that we sent to you last week.  Everyone in ")
    file.write(city + " knows what an exceptional offer this is!  ")
    file.write("(Expecially those with lovely eyes of " + eyeColor + "!  ")
    file.write("We hope to hear from you soon.\n\n")
    file.write("Sincerely,\n\n")
    file.write("I.M. Acrook, Attorney at Law")
    file.close()
