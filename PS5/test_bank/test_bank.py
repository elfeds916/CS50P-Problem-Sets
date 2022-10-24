from bank import value

def main():
    test_value_0()
    test_value_20()
    test_value_100()

def test_value_0():
    assert value("Hello") == 0
    
def test_value_20():
    assert value("How are you?") == 20

def test_value_100():
    assert value("Assalamualaikum") == 100

if __name__ == "__main__":
    main()
