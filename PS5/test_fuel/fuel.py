def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fuel_percentage = convert(fraction)
            fuel_gauge = gauge(fuel_percentage)
            print(fuel_gauge)
        except (ValueError, ZeroDivisionError):
            break

def convert(fraction):
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > 0 and y > 0 and x < y:
            fuel_percentage = int(round((x / y) * 100, 0))
        elif y == 0:
            raise ZeroDivisionError
        else:
            raise ValueError
        return fuel_percentage


def gauge(fuel_percentage):
    if fuel_percentage <= 1:
        return "E"
    elif fuel_percentage >= 99:
        return "F"
    else:
        return f"{fuel_percentage}%"


if __name__ == "__main__":
    main()