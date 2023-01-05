print("Welcome to the time calculator.")

total = float(input("What is the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

amount = round(total * (1 + tip / 100) / people, 2)

print(f"The amount you should pay is ${amount}")