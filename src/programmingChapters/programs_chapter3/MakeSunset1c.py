def makeSunset(fileName):
    picture = makePicture(fileName)
    for p in getPixels(picture):
        setBlue(p, getBlue(p) * 0.7)
        setGreen(p, getGreen(p) * 0.7)
    return picture
