import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Checks to make sure that the string is wrapped inside the iframe tag
    if re.search(r"<iframe(.)*><\/iframe>", s):
        # REGEX with grouping to get the video ID in youtube
        src = re.search(r"(http)s?:\/\/(www\.)?youtube\.com\/embed\/(\w+)", s)
        if src:
            # String concatination using fstring
            return f"https://youtu.be/{src.group(3)}"
        else:
            return None

if __name__ == "__main__":
    main()