import pytest
from lines2 import no_of_lines

def main():
    test_no_of_lines()

def test_no_of_lines():
    assert no_of_lines("asdfg.py") == "File does not exists"
    assert no_of_lines("") == "Too few command-line arguments"
    assert no_of_lines("file1.py file2.py") == "Too many command-line arguments"
    assert no_of_lines("filename.txt") == "Not a Python file"
    assert no_of_lines("bitcoin.py") == 17

if __name__ == "__main__":
    main()
