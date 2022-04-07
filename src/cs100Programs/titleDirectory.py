import os

def titleDirectory(dir):
    for file in os.listdir(dir):
        print "Processing: ", dir + "//" + file # "//" puts in the right path delimiter for the current OS
        if file.endswith(".jpg"):
            picture = makePicture(dir + "//" + file)
            addText(picture, 10, 20, "Property of CS100 at BYU")
            writePictureTo(picture, dir+"//"+"titled-" + file)
