import re

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    try:
        f, s, t, l = ip.split(".", maxsplit=4)
        if f.isalpha() == True or s.isalpha() == True or t.isalpha() == True or l.isalpha() == True:
            return False
        if int(f) > 255 or int(f) < 0:
            return False
        if int(s) > 255 or int(s) < 0:
            return False
        if int(t) > 255 or int(t) < 0:
            return False
        if int(l) > 255 or int(l) < 0:
            return False
        else:
            return True
    except:
        return False

if __name__ == "__main__":
    main()