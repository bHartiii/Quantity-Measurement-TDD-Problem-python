import pytest

from com.bridgelabz.quantity_measurement.length_type import Lengths
from com.bridgelabz.quantity_measurement.quantity_measurement import LengthConvertor
from com.bridgelabz.quantity_measurement.quantity_measurement_error import QuantityMeasurementError


# check if given two enum members with some value are equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Lengths.FEET, 1.0, Lengths.FEET),
    (2.0, Lengths.CM, 2.0, Lengths.CM),
    (1.0, Lengths.INCH, 1.0, Lengths.INCH),
    (1.0, Lengths.YARD, 1.0, Lengths.YARD),
    (1.0, Lengths.FEET, 12.0, Lengths.INCH),
    (12.0, Lengths.INCH, 1.0, Lengths.FEET),
    (36.0, Lengths.INCH, 1.0, Lengths.YARD),
    (1.0, Lengths.YARD, 36.0, Lengths.INCH),
    (1.0, Lengths.YARD, 3.0, Lengths.FEET),
    (3.0, Lengths.FEET, 1.0, Lengths.YARD),
    (2.0, Lengths.INCH, 5.0, Lengths.CM),
    (5.0, Lengths.CM, 2.0, Lengths.INCH),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_ShouldReturn_True(value1, unit1, value2, unit2):
    assert LengthConvertor(value1, unit1) == LengthConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Lengths.FEET, 2.0, Lengths.FEET),
    (2.0, Lengths.CM, 1.0, Lengths.CM),
    (1.0, Lengths.INCH, 2.0, Lengths.INCH),
    (1.0, Lengths.YARD, 2.0, Lengths.YARD),
    (1.0, Lengths.FEET, 1.0, Lengths.INCH),
    (12.0, Lengths.INCH, 12.0, Lengths.FEET),
    (36.0, Lengths.INCH, 36.0, Lengths.YARD),
    (1.0, Lengths.YARD, 6.0, Lengths.INCH),
    (1.0, Lengths.YARD, 1.0, Lengths.FEET),
    (3.0, Lengths.FEET, 3.0, Lengths.YARD),
    (2.0, Lengths.INCH, 2.0, Lengths.CM),
    (5.0, Lengths.CM, 5.0, Lengths.INCH),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_ShouldReturn_False(value1, unit1, value2, unit2):
    assert LengthConvertor(value1, unit1) != LengthConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2, expected", [
    (2.0, Lengths.INCH, 2.0, Lengths.INCH, 4),
    (1.0, Lengths.FEET, 2.0, Lengths.INCH, 14),
    (1.0, Lengths.FEET, 1.0, Lengths.FEET, 24),
    (2.0, Lengths.INCH, 2.5, Lengths.CM, 3),
])
def test_GivenTwoEnumWithSomeValue_WhenAdded_ShouldReturn_Expected(value1, unit1, value2, unit2, expected):
    assert LengthConvertor(value1, unit1) + LengthConvertor(value2, unit2) == expected
