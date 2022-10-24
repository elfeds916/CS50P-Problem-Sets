import sys
import requests

# If file is executed without an argument
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

# If arguments is not covertible to float i.e. strings or letters
elif sys.argv[1].isalpha() == True:
    sys.exit("Command-line argument is not a number")

# Argument is a digit, an integer or a float   
else:
    try:
        # Defining a variable to store sys.argv[1]
        amount = sys.argv[1]
        amount = float(amount)

        # Getting data from the web and converts it into a json file "r"
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r = r.json()

        # Accessing the rate from the json dictionary "r" inside another dictionary
        rate = r["bpi"]["USD"]["rate_float"]
        cost = amount * rate

        # Printing the total cost with 4 decimal places
        print(f"${cost:,.4f}")
        
    except requests.RequestException:
        sys.exit("RequestException")