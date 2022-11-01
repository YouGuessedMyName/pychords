from concrete_chord import ConcreteChord, from_notes
from theoretical_chord import TheoreticalChord
from notes import CN, TN
from chords import *
import unittest
from transpose import *
import modes

class TestConcreteChord(unittest.TestCase):

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
        Cmajor = TheoreticalChord(TN._1, MAJOR)
        self.assertEqual(Cmajor.notes(), [TN._1, TN._3, TN._5])
        Gminor = TheoreticalChord(TN._5, MINOR)
        self.assertEqual(Gminor.notes(), [TN._5, TN._7b, TN._2])

class TestNote(unittest.TestCase):

    def test_parse(self):
        Bb = CN.parse("Bb")
        self.assertEqual(Bb, CN.AS)

class TestTransposition(unittest.TestCase):

    def test_transpose(self):
        tcc = transpose_from_to_key(ConcreteChord(CN.A, chords.MINOR), CN.C, CN.F)
        self.assertEqual(str(tcc), str(ConcreteChord(CN.D, chords.MINOR)))

class TestFindChord(unittest.TestCase):

    def test_find_chord(self):
        m_notes = chords.MAJOR.notes
        m2 = chords.find_chord(m_notes)
        self.assertEqual(m2.name, "Major")
    
    def test_from_notes(self):
        self.assertTrue(CN.C == CN.C)
        Cmajor = ConcreteChord(CN.C, MAJOR)
        notes = Cmajor.notes()
        self.assertEqual(notes, [CN.C, CN.E, CN.G])
        Cmajor2 = from_notes(Cmajor.root_note, notes)
        self.assertEqual(str(Cmajor), str(Cmajor2))


if __name__ == "__main__":
    unittest.main()