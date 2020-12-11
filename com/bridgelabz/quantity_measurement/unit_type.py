import enum


class Length(enum.Enum):
    # units for length
    INCH = 1
    FEET = 12
    CM = 0.4
    YARD = 36

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Volume(enum.Enum):
    # units for volume
    LITRE = 1
    GALLON = 3.78
    ML = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Weight(enum.Enum):
    KG = 1
    GM = 0.001
    TONNE = 1000

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Temp(enum.Enum):
    # units for temperature
    F = 212
    C = 100

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        if self.unit == Temp.C.value:
            return value*9/5 + 32
        elif self.unit == Temp.F.value:
            return value*self.unit/212


