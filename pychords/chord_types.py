from enum import Enum
from collections import namedtuple
from itertools import permutations
from typing import List

from pychords.notes import CN, TN

# Chords are defined as a list that contains all notes

class Spelling(Enum):
    FLAT = -1
    SHARP = 1

# Determines whether it should be denoted as F# or Gb
FS_GB_spelling = Spelling.FLAT

# Special type 
ChordType = namedtuple("ChordType", ["name", "notes", "spelling", "exceptions", "short"])

# This list keeps track of all known chords (e.g. major, minor)
chord_types_list = []

def add(chord: ChordType, add_inversions=True) -> ChordType:
    """Add a new chord type.

    Args:
        chord (Chord)

    Returns:
        Chord: chord
    """
    
    # Add inversions
    if add_inversions:
        notes = chord.notes.copy()
        for perm, spelling in zip(permutations(notes), permutations(chord.spelling)):
            inv_chord = ChordType(chord.name, perm, spelling, chord.exceptions, chord.short)
            chord_types_list.append(inv_chord)
    else:
        # Add canon inversion only
        chord_types_list.append(tuple(chord))
    
    return chord

def find_chord(notes: List) -> ChordType:
    """Find a chord using its notes

    Args:
        notes (List): List of TN (theoretical note) objects

    Returns:
        Chord: chord
    """
    # Find the index of these notes and then return
    notes_list = list(map(lambda x: tuple(x.notes), chord_types_list))
    try:
        i = notes_list.index(tuple(notes))
        return chord_types_list[i]
    except ValueError:
        return ChordType("Unknown", notes, [Spelling.FLAT for x in notes], {}, "u")

MAJOR_CHORD = add(ChordType("Major", [TN._1, TN._3, TN._5], [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT], {CN.FS.value: FS_GB_spelling}, ""))
MINOR_CHORD = add(ChordType("Minor", [TN._1, TN._3b, TN._5], [Spelling.SHARP, Spelling.FLAT, Spelling.SHARP], {CN.DS.value: FS_GB_spelling}, "m"))