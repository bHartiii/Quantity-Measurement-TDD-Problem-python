import pytest

from com.bridgelabz.quantity_measurement.length_adder import LengthAdder
from com.bridgelabz.quantity_measurement.length_type import Lengths
from com.bridgelabz.quantity_measurement.length_convertor import LengthConvertor
from com.bridgelabz.quantity_measurement.quantity_measurement_error import QuantityMeasurementError

# convertors to compare one length type to other
Self_To_Self = "Self_To_Self"
Inch_To_Feet = "Inch_To_Feet"
Feet_To_Inch = "Feet_To_Inch"
Yard_To_Feet = "Yard_To_Feet"
Feet_To_Yard = "Feet_To_Yard"
Yard_To_Inch = "Yard_To_Inch"
Inch_To_Yard = "Inch_To_Yard"
Inch_To_Centimeter = "Inch_To_Centimeter"
Centimeter_To_Inch = "Centimeter_To_Inch"
ft = "feet"
inch = "inch"
cm = "centimeter"


# check if given two enum members with some value are equal or not
@pytest.mark.parametrize("value1, value2, converter, expected", [
    (1.0, 1.0, Self_To_Self, True),
    (2.0, 1.0, Self_To_Self, False),
    (1.0, 1.0, Feet_To_Inch, False),
    (1.0, 1.0, Feet_To_Yard, False),
    (1.0, 1.0, Inch_To_Yard, False),
    (3.0, 1.0, Feet_To_Yard, True),
    (1.0, 12.0, Feet_To_Inch, True),
    (1.0, 36.0, Yard_To_Inch, True),
    (36.0, 1.0, Inch_To_Yard, True),
    (1.0, 3.0, Yard_To_Feet, True),
    (1.0, 12.5, Feet_To_Inch, False),
    (1.0, 12.5, Yard_To_Feet, False),
    (1.0, 12.5, Feet_To_Yard, False),
    (1.0, 12.5, Yard_To_Inch, False),
    (1.0, 12.5, Inch_To_Feet, False),
    (1.0, 12.5, Inch_To_Yard, False),
    (1, 12, Feet_To_Inch, True),
    (1, 20, Feet_To_Inch, False),
    (1, 2, Inch_To_Centimeter, False),
    (2, 5, Inch_To_Centimeter, True),
    (1, 2, Centimeter_To_Inch, False),
    (5, 2, Centimeter_To_Inch, True),

])
def test_GivenTwoEnumWithSomeValue_WhenCompared_ShouldReturn_Expected(value1, value2, converter, expected):
    assert LengthConvertor(value1, value2, converter).__eq__(Lengths) == expected


def test_GivenTwoInchLengthTypes_WhenAdded_ShouldReturnSumInInches():
    length_convertor = LengthConvertor(2, 2, Self_To_Self)
    assert LengthAdder(length_convertor).add_length_in_inches(inch, inch) == 4


def test_GivenFeetAndInchLengthTypes_WhenAdded_ShouldReturnSumInInches():
    length_convertor = LengthConvertor(1, 2, Feet_To_Inch)
    assert LengthAdder(length_convertor).add_length_in_inches(ft, inch) == 14


def test_GivenTwoFeetLengthTypes_WhenAdded_ShouldReturnSumInInches():
    length_convertor = LengthConvertor(1, 1, Feet_To_Inch)
    assert LengthAdder(length_convertor).add_length_in_inches(ft, ft) == 24
