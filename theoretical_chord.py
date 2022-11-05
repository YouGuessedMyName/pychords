from abstract_chord import AbstractChord, abstract_chord_from_notes
from notes import TN
from chords import Chord
from typing import List

class TheoreticalChord(AbstractChord):
    def __init__(self, root_note: TN, chord: Chord) -> None:
        super().__init__(root_note, chord, TN)
    
    def spell(self) -> List:
        """Spell the chord, i.e. enumerate the notes

        Example: (for A Major) ["A, C#, E"]
        """
        return [x.spell_flat() for x in self.notes()]

def from_notes(root_note: TN, notes: List) -> TheoreticalChord:
    (root_note, chord) = abstract_chord_from_notes(root_note, notes)
    return TheoreticalChord(root_note, chord)