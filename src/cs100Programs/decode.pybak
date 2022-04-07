def decode(encodedImg):
    message = makeEmptyPicture(getWidth(encodedImg), getHeight(encodedImg))
    for x in range(0, getWidth(encodedImg)):
        for y in range(0, getHeight(encodedImg)):
            encPx1 = getPixel(encodedImg, x, y)
            msgPx1 = getPixel(message, x, y)
            if getRed(encPx1) % 2 == 1:
                setColor(msgPx1, black)
    return message
