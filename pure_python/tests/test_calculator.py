import pytest
from pure_python.calculator import Calculator



def test_sum():
    calc = Calculator(48, 34)
    assert calc.sum() == 82


def test_subtract():
    calc = Calculator(89, 3)
    assert calc.subtract() == 86


def test_multiply():
    calc = Calculator(45, 2)
    assert calc.multiply() == 90


def test_divide():
    calc = Calculator(16, 2)
    assert calc.divide() == 8


def test_divide_by_zero():
    calc = Calculator(18, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()


def test_getters_setters():
    calc = Calculator(1, 2)
    calc.op1 = 10
    calc.op2 = 5
    assert calc.op1 == 10
    assert calc.op2 == 5
    assert calc.sum() == 15


def test_repr():
    calc = Calculator(15, 12)
    assert repr(calc) == "Calculator(op1=15, op2=12)"
