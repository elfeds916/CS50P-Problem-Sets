amount_due = 50
#print("Amount Due: ", amount_due)

while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due = amount_due - coin
        #if amount_due == 0:
        #    print("Change Owed: 0")
        #elif amount_due < 0:
        #    print("Change Owed: ", abs(amount_due))
        #else:
        #    print("Amount Due: ", amount_due)
   # else:
    #    print("Amount Due: ", amount_due)
     #   continue
print("Change Owed: ", abs(amount_due))