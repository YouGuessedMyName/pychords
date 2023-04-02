from concrete_chord import ConcreteChord, from_notes
from notes import CN
import modes
import chords
from concrete_scale import ConcreteScale
from theoretical_chord import TheoreticalChord
from theoretical_scale import TheoreticalScale


Cmajor = ConcreteChord(CN.C, chords.MAJOR)
notes = Cmajor.notes()

Cmajor2 = from_notes(Cmajor.root_note, notes)
