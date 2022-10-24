import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()
    test_value_error()
    test_zero_division_error()

def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("1/4") == 25
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()