#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import sys
sys.path.append("C:\\Users\\lehi\\Desktop\\CS100_lab5\\pMedia.py")
import pMedia

def clip(value):
  result = int (value)
  if result < 0:
    result = 0
  elif result > 255:
    result = 255
  return result
    
def luminance (pixel):

  red = getRed(pixel) * 0.299
  green = getGreen(pixel) * 0.587
  blue = getBlue(pixel) * 0.114
  return int (red + green + blue)
  
  
  
def adjustColorValue(colorValue, m, b):
  result = clip(colorValue * m + b)
  return result
  
def adjustPixel(pixel, m, b):
  red = adjustColorValue(getRed(pixel), m, b)
  green = adjustColorValue(getGreen(pixel), m, b)
  blue = adjustColorValue(getBlue(pixel), m, b)
  newColor = makeColor(red, green, blue)
  setColor(pixel, newColor)
  
def transform(picture, x1, y1, x2, y2):
  dx = x1 - x2
  dy = y1 - y2
  m = (float(dy))/dx
  b = (y1 - m) * x1
  for pixel in getPixels(picture):
    adjustPixel(pixel, m, b)
  
def threshold (picture, threshold):
   for pixel in getPixels(picture):
     if (luminance(pixel) <= threshold):
       setColor(pixel, black)
     else:
       setColor(pixel, white)
       
def processPicture(picture, x1, y1, x2, y2):
  if (x1 == x2):
    threshold(picture, x1)
  else:
    transform(picture, x1, y1, x2, y2)
  
def curves(filename, x1, y1, x2, y2):
  picture = makePicture(getMediaPath(filename))
  processPicture(picture, x1, y1, x2, y2)  
  return picture
  
#p2 = curves("Penguins.jpg", 0, 64, 191, 255)
#show(p2)
#writePictureTo(p2, "picture1.jpg")
#p3 = curves("Penguins.jpg", 64, 0, 255, 191)
#show(p3)
#writePictureTo(p3, "picture2.jpg")
#p4 = curves("Penguins.jpg",64,0, 191, 255)
#show(p4)
#writePictureTo(p4, "picture3.jpg")
#p5 = curves("Penguins.jpg",0 , 64, 255, 191)
#show(p5)
#writePictureTo(p5, "picture4.jpg")
#p6 = curves("Penguins.jpg", 127, 0, 127, 255)
#show(p6)
#writePictureTo(p6, "picture5.jpg")
#p7 = curves("Penguins.jpg",255, 0, 0, 255)
#show(p7)
#writePictureTo(p7, "picture6.jpg")
#p8 = curves("Penguins.jpg",96, 0, 191, 255)
#show(p8)
#writePictureTo(p8, "picture7.jpg")