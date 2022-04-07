import urllib

def findTemperatureLive():
    connection = urllib.urlopen("http://deseretnews.com/home")
    weather = connection.read()
    connection.close()

    #weatherFile = getMediaPath("desNews.html") # an html file is just a text file
    #file = open(weatherFile, "rt")
    #weather = file.read()
    #file.close()

    currLoc = weather.find("temperature")
    if currLoc == -1:
        print "They must have changed the page format -- can't find the temp"
    else:
        temploc = weather.find("&#730;", currLoc)
        tempstart = weather.rfind(">", 0, temploc)
        print "Current temperature:", weather[tempstart + 1:temploc]

if __name__ == "__main__":
    findTemperatureLive()
