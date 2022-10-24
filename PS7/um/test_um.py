import pytest
from um import count

def main():
    test_um_word()
    test_um_upper()
    test_um_within_word()

def test_um_word():
    assert count("Um, um, UM, yummy") == 3

def test_um_upper():
    assert count("UM, yummy") == 1
    assert count("INTRUMENTAL") == 0

def test_um_within_word():
    assert count("instrumental") == 0
    assert count("bumper") == 0
    assert count("PLUMBER") == 0


if __name__ == "__main__":
    main()