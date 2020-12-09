from enum import Enum

from com.bridgelabz.quantity_measurement.length_type import Lengths


class LengthConvertor:

    def __init__(self, value1, value2, convertor):
        if type(value1) != float and type(value2) != float:
            value1 = float(value1)
            value2 = float(value2)
        self.value1 = value1
        self.value2 = value2
        self.convertor = convertor

    def __eq__(self, other):
        switcher = {
            Lengths.Self_To_Self.name: Lengths.Self_To_Self.value,
            Lengths.Feet_To_Inch.name: Lengths.Feet_To_Inch.value,
            Lengths.Feet_To_Yard.name: Lengths.Feet_To_Yard.value,
            Lengths.Yard_To_Inch.name: Lengths.Yard_To_Inch.value,
            Lengths.Inch_To_Yard.name: Lengths.Inch_To_Yard.value,
            Lengths.Inch_To_Feet.name: Lengths.Inch_To_Feet.value,
            Lengths.Yard_To_Feet.name: Lengths.Yard_To_Feet.value,
            Lengths.Inch_To_Centimeter.name: Lengths.Inch_To_Centimeter.value,
            Lengths.Centimeter_To_Inch.name: Lengths.Centimeter_To_Inch.value,
        }
        return self.value1 * switcher.get(self.convertor) == self.value2