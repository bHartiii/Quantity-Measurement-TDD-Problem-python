import pytest

from com.bridgelabz.quantity_measurement.feet import Feet
from com.bridgelabz.quantity_measurement.inch import Inch
from com.bridgelabz.quantity_measurement.yard import Yard
from com.bridgelabz.quantity_measurement.quantity_measurment_error import QuantityMeasurementError


@pytest.fixture
def feet_object():
    return Feet(1.0)


def inch_object():
    return Inch(1.0)


def yard_object():
    return Yard(1.0)


# check if given instances with same value are same or not
@pytest.mark.parametrize("object1, object2", [
    (feet_object, inch_object),
    (feet_object, yard_object),
    (inch_object, yard_object),
    (feet_object, feet_object),
    (inch_object, inch_object),
    (yard_object, yard_object),

])
def test_GivenTwoInstanceWithSameValue_WhenCompared_ShouldReturnExpected(object1, object2):
    assert object1 == object2


# checks if the instances are same but values are different
def test_WhenGivenTwoFeetInstancesButDifferentValues_ShouldRaiseException():
    first_feet = Feet(2)
    second_feet = Feet(1)
    assert first_feet != second_feet


def test_WhenGivenTwoInchInstancesButDifferentValues_ShouldRaiseException():
    first_inch = Inch(2)
    second_inch = Inch(1)
    assert first_inch != second_inch


def test_WhenGivenTwoYardInstancesButDifferentValues_ShouldRaiseException():
    first_yard = Yard(2)
    second_yard = Yard(1)
    assert first_yard != second_yard


# def test_WhenGivenSameInstancesButDifferentValues_ShouldRaiseException2(feet_object, inch_object):
#     # first_feet = feet_object
#     # second_feet = inch_object
#     assert feet_object == inch_object
