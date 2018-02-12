import re
import config
import sys


# TODO : better finding of chord lines (skip empty lines etc)
# TODO : not harmonically coherent all the time (double sharp etc)


def readFromInput(filePath):
    f = open(filePath, 'r')
    r = f.read()
    f.close()
    # return r[:-1]
    return r

def writeToOutput(text):
    f = open(sys.argv[1] + ".transposed.txt", 'w')
    print(text, file = f)
    f.close()



def transpose(text, originalTone, destTone):
    result = ""
    originalScale = getScale(originalTone)
    destScale = getScale(destTone)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if isChordLine(line) :
            result += transposeLine(line, originalScale, destScale) + "\n"
        else :
            result += line + "\n"
    return result



def getScale(tone):
    scalesList = config.scales.split('\n')

    equivalentTone = None
    if tone in config.equivalent.keys() :
        equivalentTone = config.equivalent[tone]

    for scale in scalesList :
        degrees = scale.split(' ')
        if degrees[0] == tone \
            or (equivalentTone and degrees[0] == equivalentTone) :
            return degrees
    return 'Error : not a recognized tone'

def destTone(originalTone, originalScale, destScale):
    if originalTone in originalScale :
        degree = originalScale.index(originalTone)
    elif config.equivalent[originalTone] in originalScale :
        degree = originalScale.index(config.equivalent[originalTone])
    else :
        print('Error : tone ' + originalTone + ' or equivalent ' + config.equivalent[originalTone] + ' not found in scale ' + originalScale)
    return destScale[degree]

def transposeLine(line, originalScale, destScale):
    presentTones = re.findall(config.allTones, line)
    sampleLine = line
    while presentTones :
        toneToReplace = presentTones.pop(0)
        index = sampleLine.index(toneToReplace)
        transposedTone = destTone(toneToReplace, originalScale, destScale)
        sampleLine = sampleLine[:index] + 'X'*len(transposedTone) + sampleLine[index + len(toneToReplace):]
        line = line[:index] + transposedTone + line[index + len(toneToReplace):]
    return line

def isChordLine(line):
    """
    Return True if line is a chord line (and not lyrics or title etc.)
    """
    if line :
        tolerance = .1
        count = 0
        for c in line :
            if c not in config.chordSymbols :
                count += 1
        return count/len(line) < tolerance
    return False



songText = readFromInput(sys.argv[1])
if not sys.argv[2] in config.allTones:
    print('Error : value ' + sys.argv[2] + ' is not a tone')
elif not sys.argv[3] in config.allTones:
    print('Error : value ' + sys.argv[3] + ' is not a tone')
else :
    transposedSong = transpose(songText, sys.argv[2], sys.argv[3])
    writeToOutput(transposedSong)
