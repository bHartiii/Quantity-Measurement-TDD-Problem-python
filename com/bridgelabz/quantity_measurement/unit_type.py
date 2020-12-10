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
    ML = 100.1

    def __init__(self, unit):
        self.unit = unit

    def convert_into_base(self, value):
        return self.unit * value


