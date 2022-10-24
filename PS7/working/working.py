import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format1 = r"^(([0-9])|[0-1][0-2])(:[0-5][0-9])?[ ](AM|PM)([ ]to[ ])(([0-9])|[0-1][0-2])(:[0-5][0-9])?[ ](AM|PM)"
    match = re.search(format1, s)
    if match:
        if match.group(4) == "AM":
            if int(match.group(1)) == 12:
                hour1 = 0
            else:
                hour1 = int(match.group(1))
        
        else:
            if int(match.group(1)) == 12:
                hour1 = int(match.group(1))
            else:
                hour1 = int(match.group(1)) + 12

        if match.group(9) == "AM":
            if int(match.group(6)) == 12:
                hour2 = 0
            else:
                hour2 = int(match.group(6))
        
        else:
            if int(match.group(6)) == 12:
                hour2 = int(match.group(6))
            else:
                hour2 = int(match.group(6)) + 12

        if ":" not in s:
            return f"{hour1:02}:00{match.group(5)}{hour2:02}:00"

        return f"{hour1:02}{match.group(3)}{match.group(5)}{hour2:02}{match.group(8)}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()