def darken(picture):
  for pixel in getPixels(picture):
    color = getColor(pixel)
    darkerColor = make_darker(color)
    setColor(pixel, darkerColor)

def make_darker(color):
  decrementAmount = 50;
  red = max(0, color.getRed() - decrementAmount)
  green = max(0, color.getGreen() - decrementAmount)
  blue = max(0, color.getBlue() - decrementAmount)

  return Color(red, green, blue)