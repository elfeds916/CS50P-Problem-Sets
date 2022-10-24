import csv
import sys

def main():
    new_list = []
    check_args()
    try:
        with open(sys.argv[1], "r") as before_file:
            reader = csv.DictReader(before_file)
            for row in reader:
                # reader[row] = ['name': lname, fname, 'house': house]
                # Need to split the names into fName and lName
                lName, fName = row["name"].split(", ")
                house = row["house"]
                # Append the new_list list inserting the values of fName, lName, & house to each iteration
                new_list.append({"first": fName, "last": lName, "house": house})

        with open(sys.argv[2], "w", newline='') as new_file:
            fieldnames = ("first", "last", "house")
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in new_list:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
                
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (sys.argv[1].endswith(".csv") == False) or (sys.argv[2].endswith(".csv") == False):
        sys.exit("Not a CSV file")
    elif ".csv" not in sys.argv[1]:
        sys.ext(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()