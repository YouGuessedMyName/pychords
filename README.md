# Pychords

Pychords is a package that can be used to model music in python, in particular notes, chords and scales.
This project was started back when musicpy did not exist yet.

In order to understand how to use pychords, a basic understanding of music theory is required.

# Data structures

Pychords currently supports three main kinds of data structures, notes, chords, and scales/modes.
(Scroll down for a table with an overview of the types)

## Notes

A note is represented by an integer enum from 0 to 11. 
There are too kinds of notes: Concrete and Theoretical.
A concrete note is a note that you can play on a keybord, for example C, or Eb.
These are stored in an enum called **CN**
Note that the sharp variety of black notes are used, so A# also represents Bb.

A theoretical note is a note that is relevant to music theory notation, for example 1, or 3b.
So if the key is C minor, *theoretical* 1 corresponds to *concrete* C and 3b *theoretical* corresponds to *concrete* Eb.
These are stored in an enum called **TN**
Note that the flat variety of black notes are used, so iib also represents i#.

## Chords

### Chord types

A Chord type is a type of chord, for example major.
A ChordType is a namedtuple (from collections) that consists the following data:

* name: name of the chord type (for example "Major")
* notes: all the *theoretical* notes in the chord type, order does not matter (for example [TN._1, TN._3, TN._5])
* spelling: a list that contains how each note should be spelled if black keys are used. 
For example if you want to spell an A major chord, you would want it to be spelled A, C#, E and not A Db E.
To mitigate this, for major chords we use [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT].
When in doubt, just use flat for your whole chord type.
* spelling_exceptions: This is mainly used to determine how chords should be spelled in Gb major/ F# major or Eb minor / D# minor.
If this would not be there, then Gb major would be spelled Gb A# Db. I recommend using the value
{ CN.FS.value: FS_GB_spelling } 
which tells it to use the constant FS_GB_spelling to determine how to spell chords in this key.
* short: The short notation of this chord type. For major this is nothing, for minor this is "m" in order to get "Abm" for example.

If you want to add a new chord type, you can do this using the chord_types.add method.

### Concrete and theoretical chords

#### Concrete chord

A concrete chord is a chord that you can actually play on an instrument, for example Ab Major.
It stores a root note (in this case Ab) and a chord type (in this case Major).

#### Theoretical chord

A theoretical chord is a chord that exists in music theory notation, for example I Major.
It stores a root note (in this case I) and a chord type (in this case Major).

#### Shared features

Concrete chords and theoretical Chords have a lot in common because they both inherit from a class AbstractChord.

These objects can both be initialized using their respective __init__ function using the root note and the chord type.
They can also be initialized using concrete_chord_from_notes or theoretical_chord_form_notes, 
in which the chord will be determined from a list of notes.
For example, if you give it the notes E, C, G as input it, concrete_chord_from_notes will return a C Major concrete chord.

Here is an overview of the main methods of ConcreteChord and TheoreticalChord. More details can be found in the docstring.

* notes()
Get all the notes in the Chord.
* spell()
Get a list with string representations of each note.
* spell_note()
Get the spelling of this particular note in this chord.
This is mainly useful because it depends on the context of the chord whether a black note should be spelled flat or sharp.
* __str()__
Get a nice string rperesenntation of the chord
* short_representation()
Get a short string reperesentation of the chord

### Modes and Scales

A Mode is a list of notes that represents a mode. Examples are the Major scale and the Natural Minor scale.

Just like in the case of chords, there is a concrete and a theoretical variety.

#### Concrete scale

A scale that you can play on an instrument, for example the Bb minor scale.
It consists of a root note and a mode.

The concrete scale supports two extra methods which are useful:

* theoretical_chord_of(cc: ConcreteChord) Takes a concrete chord and converts it to a theoretical chord for this scale.
So for example, a D minor ConcreteChord in the ConcreteScale C major would convert to TheoreticalChord ii minor.
* concrete_chord_of(tc: TheoreticalChord) Does the oposite of the previous method: Takes a theoretical chord and converts it to a concrete chord for this scale.
So for example, a ii minor TheoreticalChord in the ConcreteScale C major would convert to ConcreteChord D minor.

#### Theoretical scale

A theoretical scale is the representation of a scale in music theory.
You might ask yourself what the difference between this and a mode is.
In fact, they store the same information and you can always convert one to the other.
However, Theoretical scale contains many useful methods that mode does not have as it's just a list.

#### Shared features

* notes()
Get all the notes in the scale.
* spell()
Get a list with string representations of each note.
* __str()__
Get a nice string rperesenntation of the scale.
* short_representation()
Get a short string reperesentation of the scale.

## transpose

Transpose is a small library of utility functions used for transposing. It currently has:

* transpose_from_to_scale Takes a concrete chord and two concrete scales and puts the chord which was in the first scale at the same theoretical place in the second scale.
For example if my input is (D minor chord, C major scale, G major scale), then the output is A minor chord, because D is the second chord in C, and A is the second chord in G
* transpose_form_to_key Does the same as the previous method, however notes are used as arguments instead of ConcreteScales.
For example if my input is (D minor chord, CN.C, CN.G) then the output is A minor chord.


## A table for reference

|  | **Chords** | **Scales** | **Notes** |
|--|------------|-----------|---------------|
| Concrete | ConcreteChord | ConcreteScale | ConcreteNote (CN) |
| Theoretical | TheoreticalChord | TheoreticalScale | TheoreticalNote (TN) |
| Type | ChordType | Mode | int |
