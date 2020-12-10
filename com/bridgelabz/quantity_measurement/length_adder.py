from com.bridgelabz.quantity_measurement.length_type import Lengths


class LengthAdder:
    def __init__(self, obj):
        self.object = obj

    def add_length_in_inches(self, length_type1, length_type2):
        if self.object.convertor == Lengths.Self_To_Self.name:
            sum = self.object.value1 + self.object.value2
        if self.object.convertor == Lengths.Feet_To_Inch.name:
            sum = self.object.value1 * Lengths.Feet_To_Inch.value + self.object.value2
        return sum


# if __name__ == "__main__":
#     length = LengthConvertor(1,2,"Feet_To_Inch")
#     print(LengthAdder(length).add_length())