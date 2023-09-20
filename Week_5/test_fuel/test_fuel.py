import pytest
from fuel import gauge, convert


def test_gauge():
    assert gauge(45) == "45%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"

def test_convert():
    assert convert("2/4") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_val_error():
    with pytest.raises(ValueError):
        convert("4/1")