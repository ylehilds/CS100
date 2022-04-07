def soundToText(sound, fileName):
    file = open(fileName, "wt")
    for s in getSamples(sound):
        file.write(str(getSampleValue(s))+"\n")
    file.close()
