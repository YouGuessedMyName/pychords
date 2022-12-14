from typing import List
from abstract_chord import AbstractChord, abstract_chord_from_notes
from notes import CN, TN, NO_NOTES
from chords import Chord, Spelling, find_chord

class ConcreteChord(AbstractChord):
    def __init__(self, root_note: CN, chord: Chord) -> None:
        super().__init__(root_note, chord, CN)

def from_notes(root_note: CN, notes: List) -> ConcreteChord:
    (root_note, chord) = abstract_chord_from_notes(root_note, notes)
    return ConcreteChord(root_note, chord)