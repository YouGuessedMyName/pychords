from notes import TN
from collections import namedtuple

Mode = namedtuple("Scale", ["name", "notes"])

MAJOR = [TN._1, TN._2, TN._3, TN._4, TN._5, TN._6, TN._7]
NATURAL_MINOR = [TN._1, TN._2, TN._3b, TN._4, TN._5, TN._6b, TN._7b]
CHROMATIC = [x for x in TN]
AUGMENTED = [TN._1, TN._2, TN._3, TN._5b, TN._6b, TN._7b]