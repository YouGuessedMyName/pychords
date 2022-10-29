from typing import List
from notes import Note
from chords import Chord

"""Stores the embodiment of a chord relative to a root note
"""
class ConcreteChord:
    def __init__(self, root_note: Note, chord: Chord) -> None:
        self.root_note = root_note
        self.chord = chord
    
        """Get the notes of this chord

        return: List of notes
        """
    def notes(self) -> List:
        