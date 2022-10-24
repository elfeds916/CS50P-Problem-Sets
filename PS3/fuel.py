while True:
    fuel = input("Fraction: ")
    try:
        # Split the string into 2 integer variables x and y
        x, y = fuel.split("/")
        # Convert both variables to integers
        x = int(x)
        y = int(y)
        # Check that both variables are positive integers; needs to come up with False or False to execute this line
        if x < 0 or x > y:
            continue

        fuel_percentage = int(round((x / y) * 100, 0))

    # Error handling block
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

# Check conditions to print E if < 1% and F if > 99%
if fuel_percentage <= 1:
    print("E")
elif fuel_percentage >= 99:
    print("F")
else:
    print(f"{fuel_percentage}%")