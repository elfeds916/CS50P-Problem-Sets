from seasons import check_date

def main():
    test_date()


def test_date():
    assert check_date("1990-09-16") == ("1990", "09", "16")
    assert check_date("cat") == None
    assert check_date("10000/13/32") == None
    assert check_date("September 16, 1990") == None
    assert check_date("16/09/1990") == None


if __name__ == "__main__":
    main()