import pychords.modes as modes
import pychords.chord_types as ct
from pychords.chords import ConcreteChord
from pychords.scales import ConcreteScale
from pychords.notes import CN

def transpose_from_to_scale(chord: ConcreteChord, source_scale: ConcreteScale, target_scale: ConcreteScale) -> ConcreteChord:
    tc = source_scale.theoretical_chord_of(chord)
    cc = target_scale.concrete_chord_of(tc)
    return cc

def transpose_from_to_key(chord: ConcreteChord, source_key: CN, target_key: CN) -> ConcreteChord:
    source_scale = ConcreteScale(source_key, modes.MAJOR)
    target_scale = ConcreteScale(target_key, ct.MAJOR)
    return transpose_from_to_scale(chord, source_scale, target_scale)