from abstract_scale import AbstractScale
from concrete_chord import ConcreteChord
from theoretical_chord import TheoreticalChord
from notes import CN, TN, NO_NOTES
from modes import Mode

class ConcreteScale(AbstractScale):
    def __init__(self, root_note: CN, mode: Mode) -> None:
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