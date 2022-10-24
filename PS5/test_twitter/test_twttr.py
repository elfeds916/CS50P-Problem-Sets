from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("SoulSeeker916") == "SlSkr916"
    assert shorten("hEllO, MAddIE") == "hll, Mdd"

if __name__ == "__main__":
    main()
