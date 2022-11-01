from typing import List
from abstract_chord import AbstractChord
from notes import CN, TN, NO_NOTES
from chords import Chord, Spelling, find_chord

class ConcreteChord(AbstractChord):
    def __init__(self, root_note: CN, chord: Chord) -> None:
        super().__init__(root_note, chord, CN)

def from_notes(root_note: CN, notes: List) -> ConcreteChord:
    normalized_notes = list(map(lambda x: TN((x.value - root_note.value) % NO_NOTES), notes))
    try:
        chord = find_chord(normalized_notes)
    except KeyError:
        chord = Chord("Unknown", normalized_notes, [Spelling.FLAT for x in normalized_notes], {}, "u")
    return ConcreteChord(root_note, chord)