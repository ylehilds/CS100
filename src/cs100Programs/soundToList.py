def soundToList(sound):
    list = []
    for s in getSamples(sound):
        list = list + [getSampleValue(s)]
    return list
