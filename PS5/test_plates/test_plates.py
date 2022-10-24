from plates import is_valid

def main():
    test_length_s()
    test_1st_2_elem_char()
    test_no_digits_in_between_chars()
    test_zero_leading()
    test_symbols()
    test_alphanumeric()


def test_length_s():
    assert is_valid("MM") == True
    assert is_valid("MM27FE123") == False
    assert is_valid("M") == False
    assert is_valid("") == False

def test_1st_2_elem_char():
    assert is_valid("MM") == True
    assert is_valid("M2") == False
    assert is_valid("2M") == False
    
def test_no_digits_in_between_chars():
    assert is_valid("MM27FE") == False
    assert is_valid("MMFE27") == True

def test_zero_leading():
    assert is_valid("MM0627") == False
    assert is_valid("MM27") == True

def test_symbols():
    assert is_valid("!@#.,") == False

def test_alphanumeric():
    assert is_valid("MMFE27") == True
    assert is_valid("123ABC") == False
    assert is_valid("MM 123") == False


if __name__ == "__main__":
    main()