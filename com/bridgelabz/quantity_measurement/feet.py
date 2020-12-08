from com.bridgelabz.quantity_measurement.inch import Inch
from com.bridgelabz.quantity_measurement.yard import Yard


class Feet:

    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            if other.feet == self.feet:
                return True
        elif isinstance(other, Yard):
            if other.yard == self.feet/3:
                return True
        elif isinstance(other, Inch):
            if other.inch == self.feet*12:
                return True

        return False

