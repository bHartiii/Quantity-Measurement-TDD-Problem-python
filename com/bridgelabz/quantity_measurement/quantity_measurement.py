from com.bridgelabz.quantity_measurement.quantity_measurement_error import QuantityMeasurementError


class UnitConvertor:
    def __init__(self, value, ob):
        self.value = value
        self.ob = ob

    def __eq__(self, other):
        if isinstance(other, UnitConvertor):
            try:
                if type(self.ob) == type(other.ob):
                    if self.ob.convert_into_base(self.value) == other.ob.convert_into_base(other.value):
                        return True
                else:
                    raise QuantityMeasurementError("Invalid Comparison")
            except QuantityMeasurementError:
                raise QuantityMeasurementError("Invalid comparison")
        return False

    def __add__(self, other):
        if isinstance(other, UnitConvertor):
            return self.ob.convert_into_base(self.value) + other.ob.convert_into_base(other.value)
