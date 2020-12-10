import pytest

from com.bridgelabz.quantity_measurement.unit_type import Length, Volume
from com.bridgelabz.quantity_measurement.quantity_measurement import UnitConvertor
from com.bridgelabz.quantity_measurement.quantity_measurement_error import QuantityMeasurementError


# check if given two enum members with some value are equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Length.FEET, 1.0, Length.FEET),
    (2.0, Length.CM, 2.0, Length.CM),
    (1.0, Length.INCH, 1.0, Length.INCH),
    (1.0, Length.YARD, 1.0, Length.YARD),
    (1.0, Length.FEET, 12.0, Length.INCH),
    (12.0, Length.INCH, 1.0, Length.FEET),
    (36.0, Length.INCH, 1.0, Length.YARD),
    (1.0, Length.YARD, 36.0, Length.INCH),
    (1.0, Length.YARD, 3.0, Length.FEET),
    (3.0, Length.FEET, 1.0, Length.YARD),
    (2.0, Length.INCH, 5.0, Length.CM),
    (5.0, Length.CM, 2.0, Length.INCH),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_ShouldReturn_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Length.FEET, 2.0, Length.FEET),
    (2.0, Length.CM, 1.0, Length.CM),
    (1.0, Length.INCH, 2.0, Length.INCH),
    (1.0, Length.YARD, 2.0, Length.YARD),
    (1.0, Length.FEET, 1.0, Length.INCH),
    (12.0, Length.INCH, 12.0, Length.FEET),
    (36.0, Length.INCH, 36.0, Length.YARD),
    (1.0, Length.YARD, 6.0, Length.INCH),
    (1.0, Length.YARD, 1.0, Length.FEET),
    (3.0, Length.FEET, 3.0, Length.YARD),
    (2.0, Length.INCH, 2.0, Length.CM),
    (5.0, Length.CM, 5.0, Length.INCH),
    (5, Length.CM, 5, Length.INCH),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_ShouldReturn_False(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) != UnitConvertor(value2, unit2)


# checks if two length type is added then sun in inches is equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2, expected", [
    (2.0, Length.INCH, 2.0, Length.INCH, 4),
    (1.0, Length.FEET, 2.0, Length.INCH, 14),
    (1.0, Length.FEET, 1.0, Length.FEET, 24),
    (2.0, Length.INCH, 2.5, Length.CM, 3),
])
def test_GivenTwoEnumWithSomeValue_WhenAdded_ShouldReturn_Expected(value1, unit1, value2, unit2, expected):
    assert UnitConvertor(value1, unit1) + UnitConvertor(value2, unit2) == expected


# checks if the comparison is valid or not(EX : Comparison of litre to inch is invalid)
@pytest.mark.parametrize("value1, unit1, value2, unit2, expected", [
    (1.0, Length.INCH, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.FEET, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.YARD, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.CM, 1.0, Volume.GALLON, QuantityMeasurementError),
    (1.0, Length.CM, 1.0, Volume.ML, QuantityMeasurementError),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_IfInvalid_ShouldRaiseException(value1, unit1, value2, unit2, expected):
    with pytest.raises(expected):
        return UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


# check if two volume units are equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Volume.LITRE, 1.0, Volume.LITRE),
    (1.0, Volume.GALLON, 1.0, Volume.GALLON),
    (1.0, Volume.ML, 1.0, Volume.ML),
    (1000.0, Volume.ML, 1.0, Volume.LITRE),
    (1.0, Volume.GALLON, 3.78, Volume.LITRE),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_IfEqual_ShouldRaise_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Volume.LITRE, 2.0, Volume.LITRE),
    (1.0, Volume.GALLON, 2.0, Volume.GALLON),
    (1.0, Volume.ML, 2.0, Volume.ML),
    (1000.0, Volume.ML, 2.0, Volume.LITRE),
    (2.0, Volume.GALLON, 3.78, Volume.LITRE),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_IfEqual_ShouldRaise_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) != UnitConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2 ,expected", [
    (1.0, Volume.LITRE, 2.0, Volume.LITRE, 3.0),
    (1.0, Volume.GALLON, 2.0, Volume.GALLON, 11.34),
    (1.0, Volume.ML, 2.0, Volume.ML, 0.003),
    (1000.0, Volume.ML, 1.0, Volume.LITRE, 2.0),
    (1.0, Volume.GALLON, 3.78, Volume.LITRE, 7.56),
])
def test_GivenTwoVolumeUnitsWithSomeValue_WhenAdded_ShouldReturn_Expected(value1, unit1, value2, unit2, expected):
    assert UnitConvertor(value1, unit1) + UnitConvertor(value2, unit2) == expected
