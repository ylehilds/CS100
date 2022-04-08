def makeSunset(picture):
    reduceBlue(picture)
    reduceGreen(picture)

def reduceBlue():
    mypic = "C:/Users/lehi/Desktop/extra/test.gif"
    picture = makePicture(mypic) 
    pixels = getPixels(mypic)
    for p in pixels:
        setBlue(p, getBlue(p) * 0.7)

def reduceGreen(picture):
    pixels = getPixels(picture)
    for p in pixels:
        setGreen(p, getGreen(p) * 0.7)
