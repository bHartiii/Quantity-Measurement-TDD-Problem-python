from enum import Enum

from com.bridgelabz.quantity_measurement.length_type import Lengths


class LengthConvertor:

    def __init__(self, value1, value2, convertor):
        self.value1 = value1
        self.value2 = value2
        self.convertor = convertor

    def __eq__(self, other):
        if self.convertor == Lengths.Self_To_Self.name:
            return self.value1 * Lengths.Self_To_Self.value == self.value2
        if self.convertor == Lengths.Feet_To_Inch.name:
            return self.value1 * Lengths.Feet_To_Inch.value == self.value2
        if self.convertor == Lengths.Feet_To_Yard.name:
            return self.value1 * Lengths.Feet_To_Yard.value == self.value2
        if self.convertor == Lengths.Yard_To_Inch.name:
            return self.value1 * Lengths.Yard_To_Inch.value == self.value2
        if self.convertor == Lengths.Inch_To_Yard.name:
            return self.value1 * Lengths.Inch_To_Yard.value == self.value2
        if self.convertor == Lengths.Inch_To_Feet.name:
            return self.value1 * Lengths.Inch_To_Feet.value == self.value2
        if self.convertor == Lengths.Yard_To_Feet.name:
            return self.value1 * Lengths.Yard_To_Feet.value == self.value2
        return False

# if __name__ == "__main__":
#     length = LengthConvertor(1.0, 1, "Feet_To_Feet")
#     print(length.__eq__(Enum))