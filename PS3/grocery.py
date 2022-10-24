# Define an empty dictionary of items
grocery = {}

# Continous input of items from the user
while True:
    try:
        item = input("").upper()
        # Check if item is in the dictionary: grocery. If not, add key and initiate value to 1
        if not item in grocery:
            grocery[item] = 1
        # If item is in the dictionary, increment the value with 1 everytime the same item is inputted by the user
        else:
            grocery[item] += 1
    except EOFError:
        break
# Prints the dictionary: grocery in alphabetical order with the values on the left
for k, v in sorted(grocery.items()):
    print(v, k)