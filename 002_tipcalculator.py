bill = float(input("What was the total bill? $"))
tip = int(input("What %age tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are to split the bill? "))
total = round((bill + (bill*tip/100))/people,2)
totalpay = str(total)
print("Everyone needs to pay: $" + totalpay)
print("It's paytime: ${}".format(totalpay))
