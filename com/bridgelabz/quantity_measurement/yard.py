from com.bridgelabz.quantity_measurement.inch import Inch


class Yard:
    def __init__(self, yard):
        self.yard = yard

    def __eq__(self, other):
        if isinstance(other, Inch):
            if other.inch == self.yard * 36:
                return True

        return False
