from collections import namedtuple
from pychords.notes import TN

Mode = namedtuple("Mode", ["name", "notes"])

MAJOR_MODE = Mode("Major", [TN._1, TN._2, TN._3, TN._4, TN._5, TN._6, TN._7])
NATURAL_MINOR_MODE = Mode("Minor", [TN._1, TN._2, TN._3b, TN._4, TN._5, TN._6b, TN._7b])
CHROMATIC_MODE = Mode("Chromatic", [x for x in TN])
AUGMENTED_MODE = Mode("Augmented", [TN._1, TN._2, TN._3, TN._5b, TN._6b, TN._7b])