def makeSunset(fileName):
    picture = makePicture(fileName)
    for pixel in getPixels(picture):
        reduceBlue(pixel)
        reduceGreen(pixel)
    return picture

def reduceBlue(pixel):
    setBlue(pixel, getBlue(pixel) * 0.7)

def reduceGreen(pixel):
    setGreen(pixel, getGreen(pixel) * 0.7)
