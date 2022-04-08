def makeSunset(fileName, amt):
    picture = makePicture(fileName)
    for p in getPixels(picture):
        setBlue(p, getBlue(p) * amt)
        setGreen(p, getGreen(p) * amt)
    return picture
