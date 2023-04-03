from typing import List
from collections import Counter

from pychords.notes import NO_NOTES, TN, CN, AbstractNote
from pychords.chord_types import FS_GB_spelling, Spelling
from pychords.chords import *

class AbstractScale:
    def __init__(self, root_note: AbstractNote, mode: List, note_enum) -> None:
        """Create a scale from a mode and root note

        Args:
            mode (Mode)
            root_note (CN)
        """
        self.mode = mode
        self.root_note = root_note
        self.note_enum = note_enum
    
    def spell(self) -> List:
        """Spell the scale, i.e. enumerate the notes as strings

        Example: (for A Major) [A, B, C#,... G#]
        """
        # The best way to spell a scale is the spelling that doesn't contain a note name twice.

        # Get the number of duplicate roots of each spelling
        flat_roots = [x.flat_root() for x in self.notes()]
        sharp_roots = [x.sharp_root() for x in self.notes()] 

        fc = Counter(flat_roots)
        sc = Counter(sharp_roots)

        f_dupes = max(fc.values())
        s_dupes = max(sc.values())

        if f_dupes < s_dupes:
            return [self.note_enum(x.value).spell_flat() for x in self.notes()]
        if f_dupes == s_dupes and FS_GB_spelling == Spelling.FLAT:
            return [self.note_enum(x.value).spell_flat() for x in self.notes()]
        else:
            return [self.note_enum(x.value).spell_sharp() for x in self.notes()]
    
    def notes(self) -> List:
        """Return all concrete notes of the scale
        """
        return [self.note_enum((self.root_note.value + x.value) % NO_NOTES) for x in self.mode]

    def __str__(self) -> str:
        spelling = self.spell()
        return spelling[0] + " " + self.scale.name + " Scale with notes " + " ".join(spelling)

class ConcreteScale(AbstractScale):
    def __init__(self, root_note: CN, mode: List) -> None:
        super().__init__(root_note, mode, CN)
    
    def short_representation(self) -> str:
        """Get a representation of the scale that consists of only one letter

        Returns:
            str: character
        """
        return self.spell()[0] + self.chord.short
    
    def theoretical_chord_of(self, cc: ConcreteChord) -> TheoreticalChord:
        tc_root = TN((self.root_note.value + cc.root_note.value) % NO_NOTES)
        return TheoreticalChord(tc_root, cc.chord)

    def concrete_chord_of(self, tc: TheoreticalChord) -> ConcreteChord:
        cc_root = CN((self.root_note.value - tc.root_note.value) % NO_NOTES)
        return ConcreteChord(cc_root, tc.chord)

class TheoreticalScale(AbstractScale):
    def __init__(self, mode: List) -> None:
        super().__init__(TN._1, mode, TN)
    
    def short_representation(self) -> str:
        """Get a representation of the scale that consists of only one letter

        Returns:
            str: character
        """
        return self.chord.short