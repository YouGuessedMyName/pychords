from abstract_chord import AbstractChord
from notes import CN
from chords import Chord

class ConcreteChord(AbstractChord):
    def __init__(self, root_note: CN, chord: Chord) -> None:
        super().__init__(root_note, chord, CN)