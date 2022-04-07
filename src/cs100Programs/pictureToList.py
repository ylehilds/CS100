def pictureToList(picture):
    list = []
    for p in getPixels(picture):
        list = list + [[getX(p), getY(p), getRed(p), getGreen(p), getBlue(p)]]
    return list
