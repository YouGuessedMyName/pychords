from enum import Enum
from collections import namedtuple
from notes import CN, TN
# Chords are defined as a list that contains all notes

class Spelling(Enum):
    FLAT = -1
    SHARP = 1

FS_GB_spelling = Spelling.FLAT

Chord = namedtuple("Chord", ["name", "notes", "spelling", "exceptions", "short"])

chords_list = []

def add(chord: Chord) -> Chord:
    chords_list.append(chord)
    return chord

SINGLE = add(Chord("Single", [TN._1], [Spelling.SHARP], {}, "s"))
MAJOR = add(Chord("Major", [TN._1, TN._3, TN._5], [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT], {CN.FS.value: FS_GB_spelling}, ""))
MINOR = add(Chord("Minor", [TN._1, TN._3b, TN._5], [Spelling.SHARP, Spelling.FLAT, Spelling.SHARP], {CN.DS.value: FS_GB_spelling}, "m"))