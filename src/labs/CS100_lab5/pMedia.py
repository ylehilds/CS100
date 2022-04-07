from PIL import Image
import array
import math

class Color:
    def __init__(self, red_value, green_value = None, blue_value = None):
        if green_value == None:
            self.red_value = Color.clip(red_value[0])
            self.green_value = Color.clip(red_value[1])
            self.blue_value = Color.clip(red_value[2])
        else:
            self.red_value = Color.clip(red_value)
            self.green_value = Color.clip(green_value)
            self.blue_value = Color.clip(blue_value)

    def toTuple(self):
        return (self.red_value, self.green_value, self.blue_value)

    def darken(self):
        self.red_value = Color.clip(self.red_value - 20)
        self.green_value = Color.clip(self.green_value - 20)
        self.blue_value = Color.clip(self.blue_value - 20)

    def lighten(self):
        self.red_value = Color.clip(self.red_value + 20)
        self.green_value = Color.clip(self.green_value + 20)
        self.blue_value = Color.clip(self.blue_value + 20)

    def __str__(self):
        return str(self.toTuple())

    @classmethod
    def clip(cls, value):
        result = value
        if result < 0:
            result = 0
        elif result > 255:
            result = 255
        return result
    
class Pixel:
    def __init__(self, picture, xPos, yPos):
        self.picture = picture
        self.xPos = xPos
        self.yPos = yPos

    def getColor(self):
        return Color(self.picture[self.xPos, self.yPos])

    def getRed(self):
        return self.picture[self.xPos, self.yPos][0]

    def getGreen(self):
        return self.picture[self.xPos, self.yPos][1]

    def getBlue(self):
        return self.picture[self.xPos, self.yPos][2]

    def setColor(self, color):
        self.picture[self.xPos, self.yPos] = color.toTuple()

    def setRed(self, redValue):
        oldValue = self.picture[self.xPos, self.yPos]
        newValue = (Color.clip(redValue), oldValue[1], oldValue[2])
        self.picture[self.xPos, self.yPos] = newValue

    def setGreen(self, greenValue):
        oldValue = self.picture[self.xPos, self.yPos]
        newValue = (oldValue[0], Color.clip(greenValue), oldValue[2])
        self.picture[self.xPos, self.yPos] = newValue

    def setBlue(self, blueValue):
        oldValue = self.picture[self.xPos, self.yPos]
        newValue = (oldValue[0], oldValue[1], Color.clip(blueValue))
        self.picture[self.xPos, self.yPos] = newValue

    def getX(self):
        return xPos

    def getY(self):
        return yPos

    def __str__(self):
        return str(self.getColor()) + ", " + str(self.xPos) + ", " + str(self.yPos)


class Picture(object):
    colorWrapAround = False

    def __init__(self, image):
        self.image = image
        self.values = image.load()

    @classmethod
    def makePicture(cls, filename):
        image = Image.open(filename)
        return Picture(image)

    @classmethod
    def makeEmptyPicture(cls, width, height, color = (0, 0, 0)):
        image = Image.new("RGB", (width, height), color)
        return Picture(image)

    def writePictureTo(self, path):
        self.image.save(path)

    def getHeight(self):
        return self.image.size[1]

    def getWidth(self):
        return self.image.size[0]

    def getPixel(self, xpos, ypos):
        return Pixel(self.values, xpos, ypos)

    def getPixels(self):
        result = []
        for x in range(self.getWidth()):
            for y in range(self.getHeight()):
                pixel = Pixel(self.values, x, y)
                result.append(pixel)
        return result

    def show(self):
        self.image.show()

    def duplicate(self):
        result = Picture.makeEmptyPicture(getWidth(self), getHeight(self))
        for x in range(self.getWidth()):
            for y in range(self.getHeight()):
                color = (self.values[x, y][0], self.values[x, y][1], self.values[x, y][2])
                result.values[x, y] = color
        return result

    @classmethod
    def getColorWrapAround(cls):
        return cls.colorWrapAround

    @classmethod
    def setColorWrapAround(cls, flag):
        cls.colorWrapAround = flag

def duplicatePicture(picture):
    return picture.duplicate()

def getColor(pixel):
    return pixel.getColor()

def getPixel(picture, xpos, ypos):
    return picture.getPixel(xpos, ypos)

def getPixels(picture):
    return picture.getPixels()

def getColor(pixel):
    return pixel.getColor()

def getRed(pixel):
    return pixel.getRed()

def getGreen(pixel):
    return pixel.getGreen()

def getBlue(pixel):
    return pixel.getBlue()

def getHeight(picture):
    return picture.getHeight()

def getWidth(picture):
    return picture.getWidth()

def makeColor(red, green, blue):
    return Color(red, green, blue)

def makePicture(filename):
    return Picture.makePicture(filename)

def makeEmptyPicture(width, height, color = (0,0,0)):
    return Picture.makeEmptyPicture(width, height, color)

def setColor(pixel, color):
    return pixel.setColor(color)

def setRed(pixel, value):
    return pixel.setRed(value)

def setGreen(pixel, value):
    return pixel.setGreen(value)

def setBlue(pixel, value):
    return pixel.setBlue(value)

def writePictureTo(picture, path):
    picture.writePictureTo(path)

def getColorWrapAround():
    return Picture.getColorWrapAround(flag)

def setColorWrapAround(flag):
    Picture.setColorWrapAround(flag)

def getX(pixel):
    return pixel.getX()

def getY(pixel):
    return pixel.getY()

def show(picture):
    picture.show()

def distance(color1, color2):
    redDist = color1[0] - color2[0]
    greenDist = color1[1] - color2[1]
    blueDist = color1[2] - color2[2]
    return math.sqrt(redDist*redDist + greenDist*greenDist + blueDist*blueDist)

def makeLighter(color):
    picture.makeLighter()

def makeDarker(color):
    picture.makeDarker()
    
if __name__ == '__main__':
    p = makePicture('DevynVsOrem.jpg')
    pixel = getPixel(p, 0, 570)
     
    #writePictureTo(p, 'dup.jpg')
    #d = makePicture('dup.jpg')
    #show(p)
