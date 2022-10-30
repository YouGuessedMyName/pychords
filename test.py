from concrete_chord import ConcreteChord
from theoretical_chord import TheoreticalChord
from notes import CN, TN
from chords import *
import unittest

class TestChord(unittest.TestCase):

    def test_notes(self):
        Cmajor = ConcreteChord(CN.C, MAJOR)
        self.assertEqual(Cmajor.notes(), [CN.C, CN.E, CN.G])
        Gminor = ConcreteChord(CN.G, MINOR)
        self.assertEqual(Gminor.notes(), [CN.G, CN.AS, CN.D])
    
    def test_spelling(self):
        Gminor = ConcreteChord(CN.G, MINOR)
        self.assertEqual(Gminor.spell(), ["G", "Bb", "D"])
        Amajor = ConcreteChord(CN.A, MAJOR)
        self.assertEqual(Amajor.spell(), ["A", "C#", "E"])
    
    def test_spelling_exceptions(self):
        GbMajor = ConcreteChord(CN.FS, MAJOR)
        self.assertEqual(GbMajor.spell(), ["Gb", "Bb", "Db"])
    
    def test_str(self):
        Gminor = ConcreteChord(CN.G, MINOR)
        self.assertEqual(str(Gminor), "G Minor Chord with notes G Bb D")
        Amajor = ConcreteChord(CN.A, MAJOR)
        self.assertEqual(str(Amajor), "A Major Chord with notes A C# E")

class TestTheoreticalChord(unittest.TestCase):

        def test_notes(self):
            Cmajor = TheoreticalChord(TN.i, MAJOR)
            self.assertEqual(Cmajor.notes(), [TN.i, TN.iii, TN.v])
            Gminor = TheoreticalChord(TN.v, MINOR)
            self.assertEqual(Gminor.notes(), [TN.v, TN.viS, TN.ii])
    
        # def test_spelling(self):
        #     Gminor = ConcreteChord(CN.G, MINOR)
        #     self.assertEqual(Gminor.spell(), ["G", "Bb", "D"])
        #     Amajor = ConcreteChord(CN.A, MAJOR)
        #     self.assertEqual(Amajor.spell(), ["A", "C#", "E"])
        
        # def test_spelling_exceptions(self):
        #     GbMajor = ConcreteChord(CN.FS, MAJOR)
        #     self.assertEqual(GbMajor.spell(), ["Gb", "Bb", "Db"])
        
        # def test_str(self):
        #     Gminor = ConcreteChord(CN.G, MINOR)
        #     self.assertEqual(str(Gminor), "G Minor Chord with notes G Bb D")
        #     Amajor = ConcreteChord(CN.A, MAJOR)
        #     self.assertEqual(str(Amajor), "A Major Chord with notes A C# E")


if __name__ == "__main__":
    unittest.main()