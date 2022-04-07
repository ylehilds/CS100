def increaseRed(picture):
    for pixel in getPixels(picture):
        value = getRed(pixel)
        setRed(pixel, value * 1.2)