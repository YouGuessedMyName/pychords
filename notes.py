from enum import Enum

NO_NOTES = 12

class AbstractNote(Enum):
    
    def spell_sharp(self):
        """Spell this note the sharp way"""
        pass
    
    def spell_flat(self):
        """Spell this note the flat way"""
        pass

class TN(AbstractNote):
    i = 0
    iS = 1
    ii = 2
    iiS = 3
    iii = 4
    iv = 5
    ivS = 6
    v = 7
    vS = 8
    vi = 9
    viS = 10
    vii = 11

    def spell_sharp(self):
        return SHARP_THEORETICAL_NOTE_NAMES[self]
    
    def spell_flat(self):
        return FLAT_THEORETICAL_NOTE_NAMES[self]  

SHARP_THEORETICAL_NOTE_NAMES = {
    TN.i:"i",
    TN.iS:"i#",
    TN.ii:"ii",
    TN.iiS:"ii#",
    TN.iii:"iii",
    TN.iv:"iv",
    TN.ivS:"iv#",
    TN.v:"v",
    TN.vS:"v#",
    TN.vi:"vi",
    TN.viS:"vi#",
    TN.vii:"vii"
}

FLAT_THEORETICAL_NOTE_NAMES = {
    TN.i:"i",
    TN.iS:"iib",
    TN.ii:"ii",
    TN.iiS:"iiib",
    TN.iii:"iii",
    TN.iv:"iv",
    TN.ivS:"vb",
    TN.v:"v",
    TN.vS:"vib",
    TN.vi:"vi",
    TN.viS:"viib",
    TN.vii:"vii"
}

class CN(AbstractNote):
    A = 0
    AS = 1
    B = 2
    C = 3
    CS = 4
    D = 5
    DS = 6
    E = 7
    F = 8
    FS = 9
    G = 10
    GS = 11

    def spell_sharp(self):
        return SHARP_CONCRETE_NOTE_NAMES[self]
    
    def spell_flat(self):
        return FLAT_CONCRETE_NOTE_NAMES[self]

SHARP_CONCRETE_NOTE_NAMES = {
    CN.A:"A",
    CN.AS:"A#",
    CN.B:"B",
    CN.C:"C",
    CN.CS:"C#",
    CN.D:"D",
    CN.DS:"D#",
    CN.E:"E",
    CN.F:"F",
    CN.FS:"F#",
    CN.G:"G",
    CN.GS:"G#"
}

FLAT_CONCRETE_NOTE_NAMES = {
    CN.A:"A",
    CN.AS:"Bb",
    CN.B:"B",
    CN.C:"C",
    CN.CS:"Db",
    CN.D:"D",
    CN.DS:"Eb",
    CN.E:"E",
    CN.F:"F",
    CN.FS:"Gb",
    CN.G:"G",
    CN.GS:"Ab"
}