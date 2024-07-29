from arithematic import Riyazi
import pytest
obj1=Riyazi
def test_add_both_integer_argument():
    assert obj1.Add(4, 3) == 7

def test_add_both_float_argument():
    assert obj1.Add(3.0, 2.5) == 5.5

def test_add_Second_argument_must_be_float_or_integer():
    with pytest.raises(ValueError, match="Second argument must be an int or float."):
        obj1.Add(1, "a")

def test_add_First_argument_must_be_float_or_integer():
    with pytest.raises(ValueError, match="First argument must be an int or float."):
        obj1.Add("a", 1)

def test_add_Both_arguments_must_be_float_or_integer():
    with pytest.raises(ValueError, match="Both arguments must be int or float."):
        obj1.Add("a", "b")