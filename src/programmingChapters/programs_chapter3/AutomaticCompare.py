def compare(p1, p2):
  pixels1 = getPixels(p1)
  pixels2 = getPixels(p2)
  numberDifferent = 0
  for i in range(len(pixels1)):
    if 2*getRed(pixels1[i]) != getRed(pixels2[i]) and 2*getRed(pixels1[i]) + 1 != getRed(pixels2[i]):
      numberDifferent += 1
  return numberDifferent
