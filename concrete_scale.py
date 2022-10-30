from abstract_scale import AbstractScale
from notes import CN
from modes import Mode

class ConcreteScale(AbstractScale):
    def __init__(self, root_note: CN, mode: Mode) -> None:
        super().__init__(root_note, mode, CN)