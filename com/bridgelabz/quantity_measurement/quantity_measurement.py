from com.bridgelabz.quantity_measurement.quantity_measurement_error import QuantityMeasurementError
from com.bridgelabz.quantity_measurement.unit_type import Temp


class UnitConvertor:
    def __init__(self, value, ob):
        self.value = value
        self.ob = ob

    def __eq__(self, other):
        """
        compares the other object with self
        :param other: takes class instance
        :return: return boolean
        """
        if isinstance(other, UnitConvertor):
            if type(self.ob) == type(other.ob):
                return self.ob.convert(self.value) == other.ob.convert(other.value)
            raise QuantityMeasurementError("Invalid Comparison")

    def __add__(self, other):
        """
        adds the values of other object with value of self
        :param other: takes class instance
        :return: return sum of values of both objects
        """
        if isinstance(other, UnitConvertor):
            if type(self.ob) == type(other.ob):
                return self.ob.convert(self.value) + other.ob.convert(other.value)
            raise QuantityMeasurementError("Invalid addition")

