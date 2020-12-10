from com.bridgelabz.quantity_measurement.length_type import Lengths


class LengthAdder:
    def __init__(self, obj):
        self.object = obj

    def add_length_in_inches(self, length_type1, length_type2):
        if length_type1 == length_type2:
            sum_inches = (self.object.value1 + self.object.value2)*self.object.switcher.get(self.object.convertor)
        if length_type1 == "feet" and length_type2 == "inch":
            sum_inches = self.object.value1 * self.object.switcher.get(self.object.convertor) + self.object.value2
        return sum_inches