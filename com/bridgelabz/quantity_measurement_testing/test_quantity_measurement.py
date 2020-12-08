import pytest

from com.bridgelabz.quantity_measurement.feet import Feet
from com.bridgelabz.quantity_measurement.inch import Inch
from com.bridgelabz.quantity_measurement.yard import Yard
from com.bridgelabz.quantity_measurement.quantity_measurment_error import QuantityMeasurementError


@pytest.fixture
def feet_object():
    return Feet(1.0)

@pytest.fixture
def inch_object():
    return Inch(1.0)

@pytest.fixture
def yard_object():
    return Yard(1.0)


# check if given same instances with same value are equal or not
@pytest.mark.parametrize("object1, object2", [
    (feet_object, feet_object),
    (inch_object, inch_object),
    (yard_object, yard_object),

])
def test_GivenTwoSameInstanceWithSameValue_WhenCompared_ShouldReturnTrue(object1, object2):
    assert object1 == object2


# check if given different instances with same value are equal or not
@pytest.mark.parametrize("obj1, obj2", [
    (feet_object, inch_object),
    (feet_object, yard_object),
    (inch_object, yard_object),
])
def test_GivenTwoDifferentInstanceWithSameValue_WhenCompared_ShouldReturnFalse(obj1, obj2):
    assert obj1 != obj2


# checks if the instances are same but values are different
def test_GivenTwoFeetInstancesButDifferentValues_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(2)
    second_feet = Feet(1)
    assert first_feet != second_feet


def test_GivenTwoInchInstancesButDifferentValues_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(2)
    second_inch = Inch(1)
    assert first_inch != second_inch


def test_GivenTwoYardInstancesButDifferentValues_WhenCompared_ShouldReturnFalse():
    first_yard = Yard(2)
    second_yard = Yard(1)
    assert first_yard != second_yard


# checks if 3ft is equals to 1yd or not
def test_GivenFeetAndYardInstance_WhenCompared_IfYardIsThriceOfFeet_ShouldReturnTrue():
    yard = Yard(1)
    feet = Feet(3)
    assert feet == yard


# checks if 1ft is equals to 12Inches or not
def test_GivenFeetAndInchInstance_WhenCompared_IfFeetIs12TimesOfInches_ShouldReturnTrue():
    inch = Inch(12)
    feet = Feet(1)
    assert feet == inch


# checks if 1yd is equals to 36in or not
def test_GivenYardAndInchInstance_WhenCompared_IfYardIs36TimesOfInches_ShouldReturnTrue():
    inch = Inch(36)
    yard = Yard(1)
    assert yard == inch
