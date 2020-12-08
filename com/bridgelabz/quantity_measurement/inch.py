class Inch:
    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        from com.bridgelabz.quantity_measurement.yard import Yard
        if isinstance(other, Yard):
            if other.yard == self.inch / 36:
                return True
        return False
