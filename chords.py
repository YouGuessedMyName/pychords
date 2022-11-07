from enum import Enum
from collections import namedtuple
from notes import CN, TN
from typing import List
# Chords are defined as a list that contains all notes

class Spelling(Enum):
    FLAT = -1
    SHARP = 1

FS_GB_spelling = Spelling.FLAT

Chord = namedtuple("Chord", ["name", "notes", "spelling", "exceptions", "short"])

chords_list = []

def add(chord: Chord) -> Chord:
    """Add a new chord.

    Args:
        chord (Chord)

    Returns:
        Chord: chord
    """
    # Add default
    chords_list.append(chord)
    # Add inversions
    chords_list.append(chords_list.pop(0))
    return chord

def find_chord(notes: List) -> Chord:
    """Find a chord using its notes

    Args:
        notes (List): List of TN (theoretical note) objects

    Returns:
        Chord: chord
    """
    notes_list = list(map(lambda x: x.notes, chords_list))
    i = notes_list.index(notes)
    return chords_list[i]

MAJOR = add(Chord("Major", [TN._1, TN._3, TN._5], [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT], {CN.FS.value: FS_GB_spelling}, ""))
MINOR = add(Chord("Minor", [TN._1, TN._3b, TN._5], [Spelling.SHARP, Spelling.FLAT, Spelling.SHARP], {CN.DS.value: FS_GB_spelling}, "m"))