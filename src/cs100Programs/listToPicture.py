def listToPicture(list):
    picture = makePicture(getMediaPath("add.png"))
    for p in list:
        if p[0] < getWidth(picture) and p[1] < getHeight(picture):
            setColor(getPixel(picture, p[0], p[1]), makeColor(p[2], p[3], p[4]))
    return picture
