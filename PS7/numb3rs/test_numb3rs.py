from numb3rs import validate

def main():
    test_format()
    test_values()

def test_format():
    assert validate(r"127.0.0.1") == True
    assert validate(r"8.8.8.8") == True
    assert validate(r"192.168") == False
    assert validate(r"cat.dog.bird.fish") == False
    assert validate(r"192") == False
    assert validate(r"192.256.255.1") == False

def test_values():
    assert validate(r"255.255.255.0") == True
    assert validate(r"256.0.1.256") == False
    assert validate(r"-1.-1.-1.-1") == False

if __name__ == "__main()":
    main()