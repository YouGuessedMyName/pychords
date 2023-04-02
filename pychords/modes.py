from collections import namedtuple

from pychords.notes import TN

Mode = namedtuple("Scale", ["name", "notes"])

MAJOR_MODE = [TN._1, TN._2, TN._3, TN._4, TN._5, TN._6, TN._7]
NATURAL_MINOR_MODE = [TN._1, TN._2, TN._3b, TN._4, TN._5, TN._6b, TN._7b]
CHROMATIC_MODE = [x for x in TN]
AUGMENTED_MODE = [TN._1, TN._2, TN._3, TN._5b, TN._6b, TN._7b]