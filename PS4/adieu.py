import inflect                              # Import inflect module

p = inflect.engine()                        # Initialize inflect engine

names = []                                  # Create an empty list of names

while True:                                 # 4ever loop
    try:
        name = input("Name: ").title()      # User inputs a name inside a 4ever loop unless interrupted
        names.append(name)                  # Appends the existing empty list to include added names while true

    except EOFError:                        # Keyboard interrupt exception handling
        break                               # Breaks out of the while loop

print()                                     # Prints extra one line
name_list = p.join((names))                 # Create new list integrating .join function from inflect module
print("Adieu, adieu, to " + name_list)      # Prints out the output