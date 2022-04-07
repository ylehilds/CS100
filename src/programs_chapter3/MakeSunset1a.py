def makeSunset(pixels):
    for p in pixels:
        setBlue(p, getBlue(p) * 0.7)
        setGreen(p, getGreen(p) * 0.7)
