import pytest

from com.bridgelabz.quantity_measurement.unit_type import Length, Volume, Weight, Temp
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
def test_GivenTwoLengthUnitsWithSomeValue_WhenCompared_ShouldReturn_True(value1, unit1, value2, unit2):
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
def test_GivenTwoLengthUnitsWithSomeValue_WhenCompared_ShouldReturn_False(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) != UnitConvertor(value2, unit2)


# check if two volume units are equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Volume.LITRE, 1.0, Volume.LITRE),
    (1.0, Volume.GALLON, 1.0, Volume.GALLON),
    (1.0, Volume.ML, 1.0, Volume.ML),
    (1000.0, Volume.ML, 1.0, Volume.LITRE),
    (1.0, Volume.GALLON, 3.78, Volume.LITRE),
])
def test_GivenTwoVolumeUnitsWithSomeValue_WhenCompared_IfEqual_ShouldRaise_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Volume.LITRE, 2.0, Volume.LITRE),
    (1.0, Volume.GALLON, 2.0, Volume.GALLON),
    (1.0, Volume.ML, 2.0, Volume.ML),
    (1000.0, Volume.ML, 2.0, Volume.LITRE),
    (2.0, Volume.GALLON, 3.78, Volume.LITRE),
])
def test_GivenTwoVolumeWithSomeValue_WhenCompared_IfEqual_ShouldRaise_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) != UnitConvertor(value2, unit2)


# checks if given weight units are equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Weight.KG, 1000.0, Weight.GM),
    (1000.0, Weight.GM, 1.0, Weight.KG),
    (1.0, Weight.TONNE, 1000.0, Weight.KG),
    (1000.0, Weight.KG, 1.0, Weight.TONNE),
])
def test_GivenTwoWeightUnitsWithSomeValue_WhenCompared_ShouldReturn_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (2.0, Weight.KG, 1000.0, Weight.GM),
    (2000.0, Weight.GM, 1.0, Weight.KG),
    (2.0, Weight.TONNE, 1000.0, Weight.KG),
    (2000.0, Weight.KG, 1.0, Weight.TONNE),
])
def test_GivenTwoWeightUnitsWithSomeValue_WhenCompared_ShouldReturn_False(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) != UnitConvertor(value2, unit2)


# checks if given temperature units are equal or not
@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (1.0, Temp.F, 1.0, Temp.F),
    (1.0, Temp.C, 1.0, Temp.C),
    (212.0, Temp.F, 100.0, Temp.C),
    (10.0, Temp.C, 50.0, Temp.F),
])
def test_GivenTwoWeightUnitsWithSomeValue_WhenCompared_ShouldReturn_True(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


@pytest.mark.parametrize("value1, unit1, value2, unit2", [
    (2.0, Temp.C, 1.0, Temp.C),
    (200.0, Temp.F, 1.0, Temp.F),
    (2.0, Temp.C, 100.0, Temp.F),
    (212.0, Temp.F, 10.0, Temp.C),
])
def test_GivenTwoWeightUnitsWithSomeValue_WhenCompared_ShouldReturn_False(value1, unit1, value2, unit2):
    assert UnitConvertor(value1, unit1) != UnitConvertor(value2, unit2)


# checks if two length type is added then sum in inches is matched or not
@pytest.mark.parametrize("value1, unit1, value2, unit2, expected", [
    (2.0, Length.INCH, 2.0, Length.INCH, 4),
    (1.0, Length.FEET, 2.0, Length.INCH, 14),
    (1.0, Length.FEET, 1.0, Length.FEET, 24),
    (2.0, Length.INCH, 2.5, Length.CM, 3),
])
def test_GivenTwoLengthWithSomeValue_WhenAdded_ShouldReturn_Expected(value1, unit1, value2, unit2, expected):
    assert UnitConvertor(value1, unit1) + UnitConvertor(value2, unit2) == expected


# check if two volume are added then sum is matched or not
@pytest.mark.parametrize("value1, unit1, value2, unit2 ,expected", [
    (1.0, Volume.LITRE, 2.0, Volume.LITRE, 3.0),
    (1.0, Volume.GALLON, 2.0, Volume.GALLON, 11.34),
    (1.0, Volume.ML, 2.0, Volume.ML, 0.003),
    (1000.0, Volume.ML, 1.0, Volume.LITRE, 2.0),
    (1.0, Volume.GALLON, 3.78, Volume.LITRE, 7.56),
])
def test_GivenTwoVolumeUnitsWithSomeValue_WhenAdded_ShouldReturn_Expected(value1, unit1, value2, unit2, expected):
    assert UnitConvertor(value1, unit1) + UnitConvertor(value2, unit2) == expected


# check if two weight units are added then sum is matched or not
@pytest.mark.parametrize("value1, unit1, value2, unit2 ,expected", [
    (1.0, Weight.KG, 2.0, Weight.KG, 3.0),
    (1.0, Weight.GM, 2.0, Weight.GM, 0.003),
    (1.0, Weight.TONNE, 1.0, Weight.TONNE, 2000.0),
    (1.0, Weight.TONNE, 1000.0, Weight.GM, 1001),
])
def test_GivenTwoVolumeUnitsWithSomeValue_WhenAdded_ShouldReturn_Expected(value1, unit1, value2, unit2, expected):
    assert UnitConvertor(value1, unit1) + UnitConvertor(value2, unit2) == expected


# checks if the comparison is valid or not(EX : Comparison of litre to inch is invalid)
@pytest.mark.parametrize("value1, unit1, value2, unit2, expected", [
    (1.0, Length.INCH, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.FEET, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.YARD, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.CM, 1.0, Volume.GALLON, QuantityMeasurementError),
    (1.0, Length.CM, 1.0, Volume.ML, QuantityMeasurementError),
    (1.0, Length.FEET, 1.0, Weight.KG, QuantityMeasurementError),
    (1.0, Weight.KG, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Weight.TONNE, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Weight.TONNE, 1.0, Temp.F, QuantityMeasurementError),
    (1.0, Temp.F, 1.0, Length.FEET, QuantityMeasurementError),
    (1.0, Temp.C, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Weight.TONNE, 1.0, Temp.C, QuantityMeasurementError),
])
def test_GivenTwoEnumWithSomeValue_WhenCompared_IfInvalid_ShouldRaiseException(value1, unit1, value2, unit2, expected):
    with pytest.raises(expected):
        return UnitConvertor(value1, unit1) == UnitConvertor(value2, unit2)


# checks if the addition is valid or not(EX : Addition of litre to inch is invalid)
@pytest.mark.parametrize("value1, unit1, value2, unit2, expected", [
    (1.0, Length.INCH, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.FEET, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.YARD, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Length.CM, 1.0, Volume.GALLON, QuantityMeasurementError),
    (1.0, Length.CM, 1.0, Volume.ML, QuantityMeasurementError),
    (1.0, Length.FEET, 1.0, Weight.KG, QuantityMeasurementError),
    (1.0, Weight.KG, 1.0, Volume.LITRE, QuantityMeasurementError),
    (1.0, Weight.TONNE, 1.0, Volume.LITRE, QuantityMeasurementError),

])
def test_GivenTwoEnumWithSomeValue_WhenAdded_IfInvalid_ShouldRaiseException(value1, unit1, value2, unit2, expected):
    with pytest.raises(expected):
        return UnitConvertor(value1, unit1) + UnitConvertor(value2, unit2)
