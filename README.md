# chordstransposer

**chordstransposer** helps musicians by transposing the chords of a song.

## Basic usage example

If you know the original tone of the song you can choose a destination tone:

```python
# Transpose the song in song_text from C# to A:
chordstransposer.transpose(song_text, 'C#', 'A')
```

Alternatively you can specify a number of semitones to transpose by:

```python
# Transpose the song 4 semitones below (a minor third):
chordstransposer.transpose_by(song_text, -4)
```

## Song file format

The song files are just plaintext, and contain a mix of lyrics lines and chord lines, as they can be found anywhere on the internet.

For instance, this is a valid song file:

```
LOST IN THE STARS
-------------

Before Lord God made the sea and the land,
  G         G°           A-7sus      D  D+
He held all the stars in the palm of his hand
   G6/B         E7b9         A-7         A-7b5
```

_These are the first bars of Kurt Weill's [Lost in the Stars](https://www.youtube.com/watch?v=6xJ1u920c2o)_

## Installation

Using pip:

```bash
pip install chordstransposer
```

## About the harmony

**transposer** tries to follow as much as possible harmonic rules (eg. Cb instead of B when necessary). These are defined in the destination scale : for instance, if you want to transpose a song to Db, then the 3rd note of the minor scale is Fb and not E. You don't need your original file to follow these rules for this to work.

However, in [traditional notation of the chords in popular music](<https://en.wikipedia.org/wiki/Chord_names_and_symbols_(popular_music)>), we avoid writing double-flat (bb) and double-sharp (x) for the sake of readability. Here, when they should appear to be perfectly correct in terms of harmony, the double-flat and double-sharp are transposed to their most simple equivalent.
