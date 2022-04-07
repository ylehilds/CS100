def encode(message_picture, original_picture):
    # make all the red value in every pixel even
    for pixel_1 in getPixels(original_picture):
        if (getRed(pixel_1) % 2) == 1:
            setRed(pixel_1, getRed(pixel_1) - 1)

    #If a pixel in message_picture is close to black then make the red value in the corresponding picture even
    for x in range(0, getWidth(original_picture)):
        for y in range(0, getHeight(original_picture)):
            message_pixel_1 = getPixel(message_picture, x, y)
            original_picture_pixel = getPixel(original_picture, x, y)
            if distance(getColor(message_pixel_1), black) < 100.0:
                setRed(original_picture_pixel, getRed(original_picture_pixel) + 1)
