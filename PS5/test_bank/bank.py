def main():
    greeting = input("Greeting: ")
    val = value(greeting)
    print(f"${val}")

def value(greeting):
    greeting = greeting.casefold().strip()
    if greeting.startswith("hello"):
        value = 0
    elif greeting.startswith("h"):
        if greeting.startswith("hello") == False:
            value = 20
    else:
        value = 100
    return value

if __name__ == "__main__":
    main()