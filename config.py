allTones = "A#|B#|C#|D#|E#|F#|G#|Ab|Bb|Cb|Db|Eb|Fb|Gb|A|B|C|D|E|F|G"

scales = """A Bb B C C# D Eb E F F# G G#
Bb B C Db D Eb E F Gb G Ab A
B C C# D D# E F F# G G# A A#
C C# D Eb E F F# G Ab A Bb B
Db D Eb Fb F Gb G Ab A Bb B C
D Eb E F F# G Ab A Bb B C C#
Eb E F Gb G Ab A Bb Cb C Db D
E F F# G G# A A# B C C# D D#
F F# G Ab A Bb B C Db D Eb E
F# G G# A A# B C C# D D# E E#
G Ab A Bb B C C# D Eb E F F#
Ab A Bb Cb C Db D Eb Fb F Gb G"""

equivalent = {'A#': 'Bb', 'Bb': 'A#', 'B': 'Cb', 'Cb': 'B', 'B#': 'C', 'C': 'B#', 'C#': 'Db', 'Db': 'C#', 'D#': 'Eb', 'Eb': 'D#', 'E': 'Fb', 'Fb': 'E', 'E#': 'F', 'F': 'E#', 'F#': 'Gb', 'Gb': 'F#', 'G#': 'Ab', 'Ab': 'G#'}

# These can be used to generate equivalence between tones
#
# def buildEquivalent(equivalentConf):
#     equivalent = {}
#     lines = equivalentConf.split('\n')
#     for line in lines :
#         line = line.split(' ')
#         equivalent[line[0]] = line[1]
#         equivalent[line[1]] = line[0]
#     return equivalent
#
# equivalentConf = """A# Bb
# B Cb
# B# C
# C# Db
# D# Eb
# E Fb
# E# F
# F# Gb"""
#
# equivalent = buildEquivalent(equivalentConf)
