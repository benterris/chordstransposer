# transposer

**transposer** helps musicians by transposing the chords of a song.  

## Basic usage example

```bash
python transposer.py mySong.txt G Bb  # transposes the song mySong for G to B-flat
```
For instance, let's take the file `lost-in-the-stars.txt` :

```
Before Lord God made the sea and the land,
  G         G°           A-7sus      D  D+
He held all the stars in the palm of his hand
   G6/B         E7b9         A-7         A-7b5
```

You can use transposer to transpose this song in any tone you like, for instance :

```bash
python transposer.py lost-in-the-stars.txt G F# # transposes lost-in-the-stars from G to F sharp
```

You can then find in the newly created file (lost-in-the-stars.transposed.txt) :

```
Before Lord God made the sea and the land,
  F#         F#°           G#-7sus      C#  C#+
He held all the stars in the palm of his hand
   F#6/A#         D#7b9         G#-7         G#-7b5
```
*These are the first bars of Kurt Weill's [Lost in the Stars](https://www.youtube.com/watch?v=6xJ1u920c2o)*

## File format

The song file must have the following structure :  

```
One text line
One chords line
One text line
One chords line
etc.
```

Make sure to remove the additional endlines when you copy-paste from the web !
