from concrete_chord import ConcreteChord
from notes import CN
import modes
import chords
from concrete_scale import ConcreteScale
from theoretical_chord import TheoreticalChord
from theoretical_scale import TheoreticalScale

old_scale = ConcreteScale(CN.A, modes.MAJOR)
os_chord = ConcreteChord(CN.B, chords.MINOR)

new_scale = ConcreteScale(CN.D, modes.NATURAL_MINOR)
tc = old_scale.theoretical_chord_of(os_chord)
print(tc)
ns_chord = new_scale.concrete_chord_of(tc)
print(ns_chord)