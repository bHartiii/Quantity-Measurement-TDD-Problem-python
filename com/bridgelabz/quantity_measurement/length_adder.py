from com.bridgelabz.quantity_measurement.length_convertor import LengthConvertor
from com.bridgelabz.quantity_measurement.length_type import Lengths


class LengthAdder:
    def __init__(self, obj):
        self.object = obj

    def add_length(self):
        if self.object.convertor == Lengths.Self_To_Self.name:
            return self.object.value1 + self.object.value2
