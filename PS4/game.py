import random


while True:
    
    try:
        level = int(input("Level: "))    
        if level < 0:
            continue
        else:
            r_number = random.randint(1, level)

            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < 0:
                        continue
                    elif guess < r_number:
                        print("Too small!")
                        continue
                    elif guess > r_number:
                        print("Too large!")
                        continue
                    else:
                        print("Just right!")
                        quit()
                except ValueError:
                    continue
    except ValueError:
        continue