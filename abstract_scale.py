from modes import Mode
from notes import NO_NOTES, TN, CN, AbstractNote
from typing import List
from collections import Counter
from chords import FS_GB_spelling, Spelling
from concrete_chord import ConcreteChord
from theoretical_chord import TheoreticalChord

class AbstractScale:
    def __init__(self, root_note: AbstractNote, mode: Mode, note_enum) -> None:
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
    
    def chords(self) -> List:
        """Return all chords of the scale

        Returns:
            List: _description_
        """
