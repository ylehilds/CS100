def luminance (pixel):

  red = getRed(pixel) * 0.299
  green = getGreen(pixel) * 0.587
  blue = getBlue(pixel) * 0.114
  return int (red + green + blue)