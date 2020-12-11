from com.bridgelabz.quantity_measurement.quantity_measurement_error import QuantityMeasurementError


class UnitConvertor:
    def __init__(self, value, ob):
        self.value = value
        self.ob = ob

    def __eq__(self, other):
        if isinstance(other, UnitConvertor):
            if type(self.ob) == type(other.ob):
                return self.ob.convert_into_base(self.value) == other.ob.convert_into_base(other.value)
            raise QuantityMeasurementError("Invalid Comparison")

    def __add__(self, other):
        if isinstance(other, UnitConvertor):
            if type(self.ob) == type(other.ob):
                return self.ob.convert_into_base(self.value) + other.ob.convert_into_base(other.value)
            raise QuantityMeasurementError("Invalid addition")
