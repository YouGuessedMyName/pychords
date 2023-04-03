# Pychords

Pychords is a package that can be used to model music in python, in particular notes and scales.
This project was started back when musicpy did not exist yet.

In order to understand how to use pychords, a basic understanding of music theory is required.

# Data structures

Pychords currently supports three main kinds of data structures, notes, chords, and scales/modes.
(Scroll down for a table with an overview of the types)

## Notes

A note is represented by an integer enum from 0 to 11. Note that the sharp variety of black notes are used, so A# also represents Bb.
There are too kinds of notes: Concrete and Theoretical.
A concrete note is a note that you can play on a keybord, for example C, or Eb.
These are stored in an enum called **CN**

A theoretical note is a note that is relevant to music theory notation, for example 1, or 3b.
So if the key is C minor, *theoretical* 1 corresponds to *concrete* C and 3b *theoretical* corresponds to *concrete* Eb.
These are stored in an enum called **TN**

## Chords

### Chord types

A Chord type is a type of chord, for example major.
A ChordType is a namedtuple (from collections) that consists the following data:

name: name of the chord type (for example "Major")

notes: all the *theoretical* notes in the chord type, order does not matter (for example [TN._1, TN._3, TN._5])

spelling: a list that contains how each note should be spelled if black keys are used. 
For example if you want to spell an A major chord, you would want it to be spelled A, C#, E and not A Db E.
To mitigate this, for major chords we use [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT].
When in doubt, just use flat for your whole chord type.

spelling_exceptions: This is mainly used to determine how chords should be spelled in Gb major/ F# major or Eb minor / D# minor.
If this would not be there, then Gb major would be spelled Gb A# Db. I recommend using the value
{ CN.FS.value: FS_GB_spelling } 
which tells it to use the constant FS_GB_spelling to determine how to spell chords in this key.

short: The short notation of this chord type. For major this is nothing, for minor this is "m" in order to get "Abm" for example.

If you want to add a new chord type, you can do this using the chord_types.add method.

#### Concrete and theoretical chords

Concrete chords and theoretical Chords have a lot in common because they both inherit from a class Abstract Chord.
Here is an overview of the main methods that they share, more information can be found in the docstrings.

##### notes()
Get all the notes in the Chord.
##### spell()
Get a list with string representations of each note.
##### spell_note()
Get the spelling of this particular note in this chord.
This is mainly useful because it depends on the context of the chord whether a black note should be spelled flat or sharp.
##### __str()__
Get a nice string rperesenntation of the chord
##### short_representation()
Get a short string reperesentation of the chord

### Concrete chord

A concrete chord is a chord that you can actually play on an instrument, for example Ab Major.
It stores a root note (in this case Ab) and a chord type (in this case Major).


## A table for reference

|  | **Chords** | **Scales** | **Notes** |
|--|------------|-----------|---------------|
| Concrete | ConcreteChord | ConcreteScale | ConcreteNote |
| Theoretical | TheoreticalChord | TheoreticalScale | TheoreticalNote |
| Type | ChordType | Mode | int |
