from notes import CN
from modes import *
from concrete_scale import ConcreteScale
from theoretical_scale import TheoreticalScale

s = ConcreteScale(CN.A, CHROMATIC)
print(s.spell())

t = TheoreticalScale(AUGMENTED)
print(t.spell())