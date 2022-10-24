import re

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    # Variable declaration with REGEX for valid IPv4 address
    match = re.search(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)
    if match:
        return True
    return False


if __name__ == "__main__":
    main()