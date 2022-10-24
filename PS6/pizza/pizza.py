from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], "r") as csvfile:
            # Converting csvfile to a dictionary/table
            table = csv.DictReader(csvfile)
            # Using tabulate function from tabulate to generate a pretty-print table format
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")