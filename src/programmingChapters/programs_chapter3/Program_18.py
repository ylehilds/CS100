def grayScaleNew(picture):
    for pixel in getPixels(picture):
        newRed = getRed(pixel) * 0.299
        newGreen = getGreen(pixel) * 0.587
        newBlue = getBlue(pixel) * 0.114

        setColor(pixel, makeColor(newRed, newGreen, newBlue))
