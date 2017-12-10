import re

string = """Before Lord God made the sea and the land,
  F         F°           G-7sus      C  C+
He held all the stars in the palm of his hand
   F6/A         D7b9         G-7         G-7b5
And they ran through his fingers like grains of sand
        F/A              Bbmaj7 G-7   C7        F/C
And one little star felt alone
    F6/C G-/C  D7/C F°/C  C7
Then the Lord God hunted through the wide night air
         F        D°                 Bb/G       C7/E
For the little dark star on the wind down there
        F/A         D7b9        G-7       Bb-/G
And he stated and promised he'd take special care
       F/A        Bbmaj7   G-   C7           F/C
So it wouldn't get lost again
      F-6/Ab       G-7b5   C7   F7   F6
Now a man don't mind if the stars grow dim
      Db/Bb     Db/B        Ab/C       F-
And the clouds blow over and darken him
        Db-/Fb               F-
So long as the Lord God's watching over them
  Db/Bb        Db/B                Ab/C F-
Keeping track of how it all goes on
        Db-/Fb          C-/Eb    D7  Db7  C7
But I've been walking through the night and the day
    F         D°                  G-7sus        C   C+
Till my eyes get weary and my head turns grey
        F6       Db13/F#      G-7        G-7b5
And sometimes it seems maybe God's gone away
    F/A                      Bb-6
Forgetting the promise that we heard him say
   F/A                         Bb-6
   And we're lost out there in the stars
(C)          Bb/C     Bb/F         F
Little stars,     big stars,     blowing through the night
D-7          D-7  Db7       Db7  F/C                 B°
   And we're lost out there in the stars
(C)          Bb/C     Bb/F         F
Little stars,      big stars,        blowing through the night
D-7          D-/B  Db7       Ab-6/Cb  F/C    G-/Bb   A°  Ab° //
     And we're lost out there in the stars, in the stars
G-/C           G-b5/C   F            Db7/F         F6"""

# TODO : equivalent tones + si equivalent tones, pas besoin de préciser la tonalité originale ?
# TODO : better finding of chord lines
# TODO : not harmonically coherent all the time (doubel sharp etc)

scales = """A Bb B C C# D Eb E F F# G G#
Bb B C Db D Eb E F Gb G Ab A
C C# D Eb E F F# G Ab A Bb B
Db D Eb Fb F Gb G Ab A Bb B C
D Eb E F F# G Ab A Bb B C C#
Eb E F Gb G Ab A Bb Cb C Db D
E F F# G G# A A# B C C# D D#
F F# G Ab A Bb B C Db D Eb E
F# G G# A A# B C C# D D# E E#
G Ab A Bb B C C# D Eb E F F#
Ab A Bb Cb C Db D Eb Fb F Gb G"""

equivalentConf = """A# Bb
B Cb
B# C
C# Db
D# Eb
E Fb
E# F
F# Gb"""

def buildEquivalent(equivalentConf):
    equivalent = {}
    lines = equivalentConf.split('\n')
    for line in lines :
        line = line.split(' ')
        equivalent[line[0]] = line[1]
        equivalent[line[1]] = line[0]
    return equivalent

equivalent = buildEquivalent(equivalentConf)

allTones = "A#|B#|C#|D#|E#|F#|G#|Ab|Bb|Cb|Db|Eb|Fb|Gb|A|B|C|D|E|F|G"

def transpose(text, originalTone, destTone):
    result = ""
    originalScale = getScale(originalTone)
    destScale = getScale(destTone)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if i % 2 :  # if we're on a chord line, that is an odd numbered line
            result += transposeLine(line, originalScale, destScale) + "\n"
        else :
            result += line + "\n"
    return result



def getScale(tone):
    scalesList = scales.split('\n')
    for scale in scalesList :
        if scale[:len(tone)] == tone :
            return scale.split(' ')
    return 'Error : not a tone'

def destTone(originalTone, originalScale, destScale):
    if originalTone in originalScale :
        degree = originalScale.index(originalTone)
    elif equivalent[originalTone] in originalScale :
        degree = originalScale.index(equivalent[originalTone])
    else :
        print('Error : tone ' + originalTone + ' or equivalent ' + equivalent[originalTone] + ' not found in scale ' + originalScale)
    return destScale[degree]

def transposeLine(line, originalScale, destScale):
    presentTones = re.findall(allTones, line)
    sampleLine = line
    while presentTones :
        toneToReplace = presentTones.pop(0)
        index = sampleLine.index(toneToReplace)
        transposedTone = destTone(toneToReplace, originalScale, destScale)
        sampleLine = sampleLine[:index] + 'X'*len(transposedTone) + sampleLine[index + len(toneToReplace):]
        line = line[:index] + transposedTone + line[index + len(toneToReplace):]
    return line
