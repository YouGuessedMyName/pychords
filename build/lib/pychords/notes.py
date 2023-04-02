from enum import Enum

NO_NOTES = 12

class AbstractNote(Enum):
    """Abstract representation of notes, can be used in both the theoretical case and the concrete case.
    """
    def spell_sharp(self):
        """Spell this note the sharp way"""
        pass
    
    def spell_flat(self):
        """Spell this note the flat way"""
        pass
    
    def sharp_root(self):
        """Get the sharp root"""
        pass
    
    def flat_root(self):
        """Get the flat root"""
        pass

    @staticmethod
    def parse(self, s: str):
        """Parse from string"""

class TN(AbstractNote):
    """Theoretical note
    """
    _1 = 0
    _2b = 1
    _2 = 2
    _3b = 3
    _3 = 4
    _4 = 5
    _5b = 6
    _5 = 7
    _6b = 8
    _6 = 9
    _7b = 10
    _7 = 11

    def spell_sharp(self):
        return SHARP_THEORETICAL_NOTE_NAMES[self]
    
    def spell_flat(self):
        return FLAT_THEORETICAL_NOTE_NAMES[self]
    
    def sharp_root(self):
        if self in [TN._2b, TN._3b, TN._5b, TN._6b, TN._7b]:
            return TN((self.value-1) % NO_NOTES)
        return self
    
    def flat_root(self):
        if self in [TN._2b, TN._3b, TN._5b, TN._6b, TN._7b]:
            return TN((self.value+1) % NO_NOTES)
        return self
    
    @staticmethod
    def parse(s: str):
        return REVERSED_THEORETICAL_NOTE_NAMES[s]

SHARP_THEORETICAL_NOTE_NAMES = {
    TN._1:"i",
    TN._2b:"i#",
    TN._2:"ii",
    TN._3b:"ii#",
    TN._3:"iii",
    TN._4:"iv",
    TN._5b:"iv#",
    TN._5:"v",
    TN._6b:"v#",
    TN._6:"vi",
    TN._7b:"vi#",
    TN._7:"vii"
}

FLAT_THEORETICAL_NOTE_NAMES = {
    TN._1:"i",
    TN._2b:"iib",
    TN._2:"ii",
    TN._3b:"iiib",
    TN._3:"iii",
    TN._4:"iv",
    TN._5b:"vb",
    TN._5:"v",
    TN._6b:"vib",
    TN._6:"vi",
    TN._7b:"viib",
    TN._7:"vii"
}

class CN(AbstractNote):
    """Concrete note
    """
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
    
    def sharp_root(self):
        if self in [CN.AS, CN.CS, CN.DS, CN.FS, CN.GS]:
            return CN((self.value-1) % NO_NOTES)
        return self
    
    def flat_root(self):
        if self in [CN.AS, CN.CS, CN.DS, CN.FS, CN.GS]:
            return CN((self.value+1) % NO_NOTES)
        return self
    
    @staticmethod
    def parse(s: str):
        return REVERSED_CONCRETE_NOTE_NAMES[s]


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

def reverse_dict(d):
    # https://stackoverflow.com/questions/43436595/python-reverse-dictionary
    return {v: k for k, v in d.items()}

REVERSED_THEORETICAL_NOTE_NAMES = reverse_dict(SHARP_THEORETICAL_NOTE_NAMES) | reverse_dict(FLAT_THEORETICAL_NOTE_NAMES)
REVERSED_CONCRETE_NOTE_NAMES = reverse_dict(SHARP_CONCRETE_NOTE_NAMES) | reverse_dict(FLAT_CONCRETE_NOTE_NAMES)