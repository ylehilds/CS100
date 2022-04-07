def grayScale(picture):
    for pixel in getPixels(picture):
        intensity = (getRed(pixel) + getGreen(pixel) + getBlue(pixel))/3
        setColor(pixel, makeColor(intensity, intensity, intensity))