import sys

def main():
    total_lines = no_of_lines(sys.argv[1])
    print(total_lines)

def no_of_lines(file_name):
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
                no_of_lines = len(lines)
                for line in lines:
                    line = line.lstrip(" ")
                    if line.startswith("#") == True or line == "\n":
                        no_of_lines -= 1
                    else:
                        continue
        except FileNotFoundError:
            sys.exit("File does not exist")
    return no_of_lines

if __name__ == "__main__":
    main()