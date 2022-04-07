def lighten(picture):
    for x in range(0,getWidth(picture)):
        for y in range(0,getHeight(picture)):
            pixel =  getPixel(picture, x, y)
            color = getColor(pixel)
            lighter_color = makeLighter(color)
            setColor(pixel, lighter_color)