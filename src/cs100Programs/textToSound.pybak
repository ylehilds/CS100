def textToSound(fileName):
    sound = makeSound(getMediaPath("bark.wav"))
    soundIndex = 0

    file = open(fileName, "rt")
    contents = file.readlines()
    file.close()

    fileIndex = 0
    while (soundIndex < getLength(sound)) and (fileIndex < len(contents)):
        #Extra parenthesis not needed to makes it easier to read
        sample = float(contents[fileIndex])
        setSampleValueAt(sound, soundIndex, sample)
        fileIndex = fileIndex + 1
        soundIndex = soundIndex + 1

    return sound
