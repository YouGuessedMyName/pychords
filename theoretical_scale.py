from abstract_scale import AbstractScale
from notes import TN
from modes import *

class TheoreticalScale(AbstractScale):
    def __init__(self, mode: Mode) -> None:
        super().__init__(TN._1, mode, TN)
