my_greeting = str.casefold(input("Greeting: ")).strip()

if my_greeting.startswith("hello"):
    print("$0")
elif my_greeting not in "hello" and my_greeting.startswith("h"):
   print("$20")
else:
    print("$100")