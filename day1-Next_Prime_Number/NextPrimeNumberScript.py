print("Welcome to Next Prime Number! Press 'Enter' for the next prime number or 'Esc' to quit.")

num = 2

def nextPrimeNumber():
    global num

    while True:
        divBy = 2
        isPrime = True

        while divBy < num:
            if num % divBy == 0:
                isPrime = False
                break
            divBy += 1

        if isPrime == True:
            print(num)
            num += 1
            break

        num += 1

while True:
    input("Press 'Enter' for the next prime number")
    nextPrimeNumber()