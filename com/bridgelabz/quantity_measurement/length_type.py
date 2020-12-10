import enum


class Lengths(enum.Enum):
    INCH = 1
    FEET = 12
    CM = 0.4
    YARD = 36

    def __init__(self, unit):
        self.unit = unit

    def convert_into_inch(self, value):
        return self.unit * value
