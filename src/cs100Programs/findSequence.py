def findSequence(seq):
    sequencesFile = getMediaPath("parasites.txt")
    file = open(sequencesFile, "rt")
    sequences = file.read()
    file.close()

    seqLoc = sequences.find(seq)
    if seqLoc == -1:
        print "Not found"
    else:
        nameLoc = sequences.rfind(">", 0, seqLoc)
        endLine = sequences.find("\n", nameLoc)
        print "Found in ", sequences[nameLoc:endLine]
    
