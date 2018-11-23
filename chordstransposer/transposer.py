import re
import sys
from .config import ALLTONES, CHORDSYMBOLS, EQUIVALENT, SCALES


def transpose(text, from_tone, to_tone):
    """
    Given a text with words and chords, keep the words and transpose
    the chords

    Args:
        text: the lyrics and chords of the song to be transposed
        from_tone: the tone in which is the song
        to_tone: the tone to which we want to transpose the song

    Returns:
        The text of the transposed song
    """
    result = ""
    original_scale = get_scale(from_tone)
    dest_scale = get_scale(to_tone)
    lines = text.split('\n')
    for line in lines:
        if is_chord_line(line):
            result += transpose_line(line, original_scale, dest_scale) + "\n"
        else:
            result += line + "\n"
    return result


def get_scale(tone):
    """
    Find the scale associated to a tone, to make sure we write harmonically
    coherent tones (eg. in A scale, we prefer to write C# over Db)

    Args:
        tone: the tone to get the scale from (eg. 'A' to get an A scale)

    Returns:
        The scale associated to the tone
    """
    scales_list = SCALES.split('\n')

    equivalent_tone = None
    if tone in EQUIVALENT.keys():
        equivalent_tone = EQUIVALENT[tone]

    for scale in scales_list:
        degrees = scale.split(' ')
        if degrees[0] == tone \
                or (equivalent_tone and degrees[0] == equivalent_tone):
            return degrees
    return 'Error : not a recognized tone'


def dest_tone(original_tone, original_scale, dest_scale):
    """
    Find the equivalent of the original tone in the destination scale, 
    wrt the original scale
    """
    if original_tone in original_scale:
        degree = original_scale.index(original_tone)
    elif EQUIVALENT[original_tone] in original_scale:
        degree = original_scale.index(EQUIVALENT[original_tone])
    else:
        print('Error : tone ' + original_tone + ' or equivalent ' +
              EQUIVALENT[original_tone] + ' not found in scale ' + original_scale)
    return dest_scale[degree]


def transpose_line(line, original_scale, dest_scale):
    """
    Given a chord line, transpose all of its chords from the original scale
    to the destination scale
    """
    present_tones = re.findall(ALLTONES, line)
    sample_line = line
    while present_tones:
        tone_to_replace = present_tones.pop(0)
        index = sample_line.index(tone_to_replace)
        transposed_tone = dest_tone(
            tone_to_replace, original_scale, dest_scale)
        sample_line = sample_line[:index] + 'X' * \
            len(transposed_tone) + sample_line[index + len(tone_to_replace):]
        line = line[:index] + transposed_tone + \
            line[index + len(tone_to_replace):]
    return line


def is_chord_line(line):
    """
    Return True if line is a chord line (and not lyrics or title etc.),
    based on the proportion of chord-like characters in the line
    """
    if line:
        tolerance = .1
        count = 0
        for c in line:
            if c not in CHORDSYMBOLS:
                count += 1
        return count/len(line) < tolerance
    return False


def read_from_input(file_path):
    """File reading helper"""
    f = open(file_path, 'r')
    r = f.read()
    f.close()
    return r


def write_to_output(text):
    """File writing helper"""
    f = open(sys.argv[1] + ".transposed.txt", 'w')
    print(text, file=f)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise TypeError(
            'Wrong number of args: chordstransposer takes exactly 3 parameters')
    song_text = read_from_input(sys.argv[1])
    if not sys.argv[2] in ALLTONES:
        print('Error : value ' + sys.argv[2] + ' is not a tone')
    elif not sys.argv[3] in ALLTONES:
        print('Error : value ' + sys.argv[3] + ' is not a tone')
    else:
        transposed_song = transpose(song_text, sys.argv[2], sys.argv[3])
        write_to_output(transposed_song)
