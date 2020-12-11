import enum


class Length(enum.Enum):
    # units for length
    INCH = 1
    FEET = 12
    CM = 0.4
    YARD = 36

    def __init__(self, unit):
        self.unit = unit

    def convert_into_base(self, value):
        return self.unit * value


class Volume(enum.Enum):
    # units for volume
    LITRE = 1
    GALLON = 3.78
    ML = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert_into_base(self, value):
        return self.unit * value


class Weight(enum.Enum):
    KG = 1
    GM = 0.001
    TONNE = 1000

    def __init__(self, unit):
        self.unit = unit

    def convert_into_base(self, value):
        return self.unit * value


