def makeSunset(fileName):
    picture = makePicture(fileName)
    for pixel in getPixels(picture):
        changeGreen(pixel, 0.7)
        changeBlue(pixel, 0.7)
    return picture

def changeGreen(pixel, amt):
    setGreen(pixel, getGreen(pixel)*amt)

def changeBlue(pixel, amt):
    setBlue(pixel, getBlue(pixel)*amt)
