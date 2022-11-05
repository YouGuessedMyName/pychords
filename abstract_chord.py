from typing import List, Tuple
from notes import CN, NO_NOTES, TN
from chords import Chord, find_chord
from chords import Spelling
from notes import AbstractNote

class AbstractChord:
    """Stores the embodiment of a chord relative to a root note
    """
    def __init__(self, root_note: AbstractNote, chord: Chord, note_enum) -> None:
        self.root_note = root_note
        self.chord = chord
        self.note_enum = note_enum
    
    def notes(self) -> List:
        """Get the notes of this chord

        return: List of Notes
        """
        return [self.note_enum((self.root_note.value + x.value) % NO_NOTES) for x in self.chord.notes]
    
    def spell(self) -> List:
        """Spell the chord, i.e. enumerate the notes

        Example: (for A Major) ["A, C#, E"]
        """
        res = []

        # Account for spelling exceptions
        if self.root_note.value in self.chord.exceptions:
            for note in self.notes(): # Just spell everything according to the exception.
                if self.chord.exceptions[self.root_note.value] == Spelling.FLAT:
                    res.append(note.spell_flat())
                else:
                    res.append(note.spell_sharp())

        else:
            for (note, spelling) in zip(self.notes(), self.chord.spelling):
                if spelling == Spelling.FLAT:
                    res.append(note.spell_flat())
                else:
                    res.append(note.spell_sharp())
        return res
    

    def __str__(self) -> str:
        """Get the string representation of the chord

        Example: (for A Major) "A Major chord with notes A C# E"
        """
        spelling = self.spell()
        return spelling[0] + " " + self.chord.name + " Chord with notes " + " ".join(spelling)
    
    def short_representation(self) -> str:
        """Get a representation of the chord that consists of only one letter

        Returns:
            str: character
        """
        return self.spell()[0] + self.chord.short

def abstract_chord_from_notes(root_note: AbstractNote, notes: List) -> Tuple[AbstractNote, Chord]:
    """Get the root note and the chord from a list of notes

    Args:
        root_note (CN): _description_
        notes (List): _description_

    Returns:
        Tuple(AbstractNote, Chord): the parameters needed to create the chord.
    """
    # Subtract the root from everything
    normalized_notes = list(map(lambda x: TN((x.value - root_note.value) % NO_NOTES), notes))
    try:
        chord = find_chord(normalized_notes)
    except KeyError:
        chord = Chord("Unknown", normalized_notes, [Spelling.FLAT for x in normalized_notes], {}, "u")
    return (root_note, chord)