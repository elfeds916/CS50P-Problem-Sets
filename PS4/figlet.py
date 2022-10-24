# Import packages and libraries
import random
import sys
from pyfiglet import Figlet

figlet = Figlet()           # Defining a variable figlet
fonts = figlet.getFonts()   # Defining a variable fonts to contain list of fonts with figlet

if len(sys.argv) == 1:                              # Checks if user did not put any arguments
    input_string = input("Input: ")                 # Gets user input
    print("Output: ")
    figlet.setFont(font = random.choice(fonts))     # Sets the font style of the output text with random fonts from fonts
    print(figlet.renderText(input_string))          # Prints rendered text

elif len(sys.argv) == 3:                            # Checks the number of argumets to be equal to 3
    if sys.argv[1] == "-f" or sys.argv[1] == "--f": # Checks if sys.argv[1] is equal to '-f' or '--f'
        if sys.argv[2] in fonts:                    # Checks if the value of sys.argv[2] is in the list of fonts
            input_string = input("Input: ")
            print("Output: ")
            figlet.setFont(font = sys.argv[2])      # Sets the font style as per the value in sys.argv[2]
            print(figlet.renderText(input_string))
        else:
            sys.exit("Invalid usage")               # Exits if sys.argv[2] is not in the list of fonts
    else:
        sys.exit("Invalid usage")                   # Exits if sys.argv[1] is anything other than '-f' or '--f'

else:
    sys.exit("Invalid usage")                       # Exits if anything else has happened ^_^