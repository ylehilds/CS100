def soundToPicture(sound):
    picture = makePicture(getMediaPath("desert.jpg"))
    soundIndex = 0
    for p in getPixels(picture):
        if soundIndex >= getLength(sound):
            break
        sample = getSampleValueAt(sound, soundIndex)
        if sample > 1000:
            setColor(p, red)
        elif sample < -1000:
            setColor(p, blue)
        else:
            setColor(p, green)
        soundIndex = soundIndex + 1
    show(picture)
    return picture
