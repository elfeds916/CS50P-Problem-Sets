import pytest
from working import convert

def main():
    test_hours()
    test_minutes()
    test_meridiem()
    test_valueerror()


def test_hours():
    assert convert("7:00 AM to 3:00 PM") == "07:00 to 15:00"
    assert convert("1:00 PM to 9:00 PM") == "13:00 to 21:00"
    assert convert("10:00 PM to 7:00 AM") == "22:00 to 07:00"

def test_minutes():
    assert convert("7:30 AM to 3:30 PM") == "07:30 to 15:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_meridiem():
    assert convert("1:00 PM to 9:00 PM") == "13:00 to 21:00"
    assert convert("1 AM to 9 AM") == "01:00 to 09:00"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("1:00 PM 9:00 PM")
    with pytest.raises(ValueError):
        convert("1:60 PM to 9:00 AM")
    with pytest.raises(ValueError):
        convert("1:00 PM - 9:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 14:00 AM")
    with pytest.raises(ValueError):
        convert("1.30 pm to 9.30 pm")
    with pytest.raises(ValueError):
        convert("12 a.m. to 12 p.m.")

if __name__ == "__main__":
    main()