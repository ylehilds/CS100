def changeLittle(filename, newString):
    programFile = getMediaPath("littlePicture.py")
    file = open(programFile, "rt")
    contents = file.read()
    file.close()

    addPos = contents.find("addText")
    firstQuote = contents.find('"', addPos)
    endQuote = contents.find('"', firstQuote+1)

    newFile = open(getMediaPath(filename), "wt")
    newFile.write(contents[:firstQuote + 1]) # the +1 makes sure we include the quote
    newFile.write(newString)
    newFile.write(contents[endQuote:])
    newFile.close()
