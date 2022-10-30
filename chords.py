from enum import Enum
from collections import namedtuple
from notes import CN
# Chords are defined as a list that contains all notes

class Spelling(Enum):
    FLAT = -1
    SHARP = 1

FS_GB_spelling = Spelling.FLAT

Chord = namedtuple("Chord", ["name", "notes", "spelling", "exceptions"])

SINGLE = Chord("Single", [0], [Spelling.SHARP], {})
MAJOR = Chord("Major", [0, 4, 7], [Spelling.FLAT, Spelling.SHARP, Spelling.FLAT], {CN.FS.value: FS_GB_spelling})
MINOR = Chord("Minor", [0, 3, 7], [Spelling.SHARP, Spelling.FLAT, Spelling.SHARP], {CN.DS.value: FS_GB_spelling})