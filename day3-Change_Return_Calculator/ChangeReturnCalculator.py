print("Welcome to the change return calculator.")

run = True

while run == True:
    def isFloat(value):
        try:
            float(value)
            return True
        except ValueError:
            print("That is not a valid number.")

    changeDue = -1
    moneyOwed = input("Money owed: ")
    while not isFloat(moneyOwed):
        moneyOwed = input("Money owed: ")
    moneyPaid = input("Money paid: ")
    while changeDue < 0:
        while not isFloat(moneyPaid):
            moneyPaid = input("Money paid: ")
        moneyOwed = float(moneyOwed)
        moneyPaid = float(moneyPaid)
        changeDue = round(moneyPaid - moneyOwed, 2)
        if changeDue >= 0:
            break
        else:
            print("You must give more money.")
            moneyPaid = input("Money paid: ")
    print(f"Change due: {changeDue}")

    hundreds = 0
    while changeDue >= 100:
        hundreds += 1
        changeDue -= 100

    fifties = 0
    while changeDue >= 50:
        fifties += 1
        changeDue -= 50

    twenties = 0
    while changeDue >= 20:
        twenties += 1
        changeDue -= 20

    tens = 0
    while changeDue >= 10:
        tens += 1
        changeDue -= 10

    fives = 0
    while changeDue >= 5:
        fives += 1
        changeDue -= 5

    ones = 0
    while changeDue >= 1:
        ones += 1
        changeDue -= 1

    quarters = 0
    while changeDue >= 0.25:
        quarters += 1
        changeDue -= 0.25

    dimes = 0
    while changeDue >= 0.1:
        dimes += 1
        changeDue -= 0.1

    nickels = 0
    while changeDue >= 0.05:
        nickels += 1
        changeDue -= 0.05

    pennies = 0
    while changeDue >= 0.01:
        pennies += 1
        changeDue -= 0.01

    if hundreds > 0:
        print(f"Hundreds: {hundreds}")
    if fifties > 0:
        print(f"Fifties: {fifties}")
    if twenties > 0:
        print(f"Twenties: {twenties}")
    if tens > 0:
        print(f"Tens: {tens}")
    if fives > 0:
        print(f"Fives: {fives}")
    if ones > 0:
        print(f"Ones: {ones}")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")

    again = input("Would you like to go again? (Y/N) ").lower()
    if again.startswith("y"):
        run == True
    elif again.startswith("n"):
        break