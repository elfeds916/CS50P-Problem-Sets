import random


def main():
    level = get_level()
    score = 0
    for i in range(10):                                     # Loops up to 10 random addition of 2 ints
        x, y = generate_integer(level)                      # Generates random ints for x and y
        ans_sum = x + y                                     # Gets the sum of x & y
        attempts = 1                                        # Attempts counter up to 3
        while attempts <= 3:                                # Checks if user got the correct answer within 3 attempts
            try:                                            
                ans_input = int(input(f"{x} + {y} = "))     # Gets the user input of the current problem
                if ans_input == ans_sum:                    # For every correct answer, add 1 to the score
                    score += 1
                    break                                   # Breaks out of the current while loop and goes back to the for loop
                else:                                       # If user inputs wrong answer, print 'EEE' and increment attempts by 1
                    print("EEE")
                    attempts += 1
                    continue
            except ValueError:                              # If user inputs other than numbers, print 'EEE' and increment attempts by 1
                print("EEE")
                attempts += 1
                continue
        else:
            print(f"{x} + {y} = ", ans_sum)                 # Prints the correct answer if user fails after 3 attempts
            continue
    print("Score: ", score)                                 # Prints the total score


def get_level():
    while True:
        try:
            n = int(input("Level: "))                       # User inputs for the level
            if not n in [1, 2, 3]:                          # Check if user inputs a number itirated on the list
                continue
            else:                                           # If user inputs anything not in the list, program will
                break                                       # keep on asking the user
        except ValueError:
            continue
    return n


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()