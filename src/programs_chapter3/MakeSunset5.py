def makeSunset(fileName, amt):
    picture = makePicture(fileName)
    for pixel in getPixels(picture):
        changeColor(pixel, amt)
    return picture

def changeColor(pixel, amt):
    setRed(pixel, getRed(pixel) * amt[0])
    setGreen(pixel, getGreen(pixel) * amt[1])
    setBlue(pixel, getBlue(pixel) * amt[2])
