from abstract_chord import AbstractChord
from notes import TN
from chords import Chord

class TheoreticalChord(AbstractChord):
    def __init__(self, root_note: TN, chord: Chord) -> None:
        super().__init__(root_note, chord, TN)