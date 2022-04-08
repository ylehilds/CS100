def makeSunset(fileName):
    picture = makePicture(fileName)
    reduceBlue(picture)
    reduceGreen(picture)
    return picture

def reduceBlue(picture):
    for p in getPixels(picture):
        setBlue(p, getBlue(p) * 0.7)

def reduceGreen(picture):
    for p in getPixels(picture):
        setGreen(p, getGreen(p) * 0.7)
