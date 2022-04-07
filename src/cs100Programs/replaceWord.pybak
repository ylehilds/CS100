def replaceWord(fileName, originalWord, replacementWord):
    file = open(getMediaPath(fileName), "rt")
    outFile = open(getMediaPath("out-" + fileName), "wt")
    for line in file.readlines():
        newLine = line.replace(originalWord, replacementWord)
        outFile.write(newLine)
    file.close()
    outFile.close()
