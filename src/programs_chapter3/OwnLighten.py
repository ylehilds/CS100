def lighten(picture):
  for pixel in getPixels(picture):
    color = getColor(pixel)
    lighterColor = make_lighter(color)
    setColor(pixel, lighterColor)

def make_lighter(color):
  incrementAmount = 50;
  red = min(255, color.getRed() + incrementAmount)
  green = min(255, color.getGreen() + incrementAmount)
  blue = min(255, color.getBlue() + incrementAmount)

  return Color(red, green, blue)
