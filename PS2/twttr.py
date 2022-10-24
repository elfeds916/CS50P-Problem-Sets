# User inputs a string
str_input = input("Input: ")

# List of vowels
vowels = ["a", "e", "i", "o", "u"]

for c in str_input:
    if c.lower() in vowels:
        str_input = str_input.replace(c, "")

print("Output:", str_input)