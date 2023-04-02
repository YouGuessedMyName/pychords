from enum import Enum
from collections import namedtuple
from notes import CN, TN
from typing import List
from itertools import permutations
# Chords are defined as a list that contains all notes

class Spelling(Enum):
    FLAT = -1
    SHARP = 1

# Determines whether it should be denoted as F# or Gb
FS_GB_spelling = Spelling.FLAT

# Special type 
Chord = namedtuple("Chord", ["name", "notes", "spelling", "exceptions", "short"])

# This list keeps track of all known chords (e.g. major, minor)
chords_list = []

def add(chord: Chord, add_inversions=True) -> Chord:
    """Add a new chord.

    Args:
        chord (Chord)

    Returns:
        Chord: chord
    """
    
    
    # Add inversions
    if add_inversions:
        notes = chord.notes.copy()
        for perm, spelling in zip(permutations(notes), permutations(chord.spelling)):
            inv_chord = Chord(chord.name, perm, spelling, chord.exceptions, chord.short)
            chords_list.append(inv_chord)
    else:
        # Add canon inversion only
        chords_list.append(tuple(chord))
    
    return chord

def find_chord(notes: List) -> Chord:
    """Find a chord using its notes

    Args:
        notes (List): List of TN (theoretical note) objects

    Returns:
        Chord: chord
    """
    # Find the index of these notes and then return
    notes_list = list(map(lambda x: tuple(x.notes), chords_list))
    try:
        i = notes_list.index(tuple(notes))
        return chords_list[i]
    except ValueError:
        return Chord("Unknown", notes, [Spelling.FLAT for x in notes], {}, "u")

MAJOR = add(Chord("Major", [TN._1, TN._3, TN._5], [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT], {CN.FS.value: FS_GB_spelling}, ""))
MINOR = add(Chord("Minor", [TN._1, TN._3b, TN._5], [Spelling.SHARP, Spelling.FLAT, Spelling.SHARP], {CN.DS.value: FS_GB_spelling}, "m"))