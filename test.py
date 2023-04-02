import unittest
from pychords import *

class TestConcreteChord(unittest.TestCase):

    def test_notes(self):
        Cmajor = ConcreteChord(CN.C, MAJOR_CHORD)
        self.assertEqual(Cmajor.notes(), [CN.C, CN.E, CN.G])
        Gminor = ConcreteChord(CN.G, MINOR_CHORD)
        self.assertEqual(Gminor.notes(), [CN.G, CN.AS, CN.D])
    
    def test_spelling(self):
        Gminor = ConcreteChord(CN.G, MINOR_CHORD)
        self.assertEqual(Gminor.spell(), ["G", "Bb", "D"])
        Amajor = ConcreteChord(CN.A, MAJOR_CHORD)
        self.assertEqual(Amajor.spell(), ["A", "C#", "E"])
    
    def test_spelling_exceptions(self):
        GbMajor = ConcreteChord(CN.FS, MAJOR_CHORD)
        self.assertEqual(GbMajor.spell(), ["Gb", "Bb", "Db"])
    
    def test_str(self):
        Gminor = ConcreteChord(CN.G, MINOR_CHORD)
        self.assertEqual(str(Gminor), "G Minor Chord with notes G Bb D")
        Amajor = ConcreteChord(CN.A, MAJOR_CHORD)
        self.assertEqual(str(Amajor), "A Major Chord with notes A C# E")

class TestTheoreticalChord(unittest.TestCase):

    def test_notes(self):
        Cmajor = TheoreticalChord(TN._1, MAJOR_CHORD)
        self.assertEqual(Cmajor.notes(), [TN._1, TN._3, TN._5])
        Gminor = TheoreticalChord(TN._5, MINOR_CHORD)
        self.assertEqual(Gminor.notes(), [TN._5, TN._7b, TN._2])

class TestNote(unittest.TestCase):

    def test_parse(self):
        Bb = CN.parse("Bb")
        self.assertEqual(Bb, CN.AS)

class TestTransposition(unittest.TestCase):

    def test_transpose(self):
        tcc = transpose_from_to_key(ConcreteChord(CN.A, MINOR_CHORD), CN.C, CN.F)
        self.assertEqual(str(tcc), str(ConcreteChord(CN.D, MINOR_CHORD)))

class TestFindChord(unittest.TestCase):

    def test_find_chord(self):
        m_notes = MAJOR_CHORD.notes
        m2 = find_chord(m_notes)
        self.assertEqual(m2.name, "Major")
    
    def test_find_chord_inversion(self):
        m_notes = [TN._3, TN._5, TN._1]
        m2 = find_chord(m_notes)
        self.assertEqual(m2.name, "Major")
    
    def test_from_notes(self):
        Cmajor = ConcreteChord(CN.C, MAJOR_CHORD)
        notes = [CN.C, CN.E, CN.G]
        self.assertEqual(notes, [CN.C, CN.E, CN.G])
        Cmajor2 = concrete_chord_from_notes(CN.C, notes)
        self.assertEqual(str(Cmajor), str(Cmajor2))
    
    def test_find_inversions(self):
        notes = [CN.E, CN.G, CN.C]
        Cmajor2 = concrete_chord_from_notes(CN.C, notes)
        self.assertEqual("C Major Chord with notes E G C", str(Cmajor2))

if __name__ == "__main__":
    unittest.main()