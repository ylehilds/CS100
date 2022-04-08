def decreaseRed(picture):
    for pixel in getPixels(picture):
        value = getRed(pixel)
        setRed(pixel, value * 0.5)