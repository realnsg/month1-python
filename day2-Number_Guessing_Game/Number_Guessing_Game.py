import random

print("Welcome to the number guessing game!)")

play = True
guess = ""
guessCount = 0

def isInteger(guess):
    try:
        int(guess)
        return True
    except ValueError:
        return False

while play:
    print("I'm thinking of a number between 1 and 100, can you guess?")
    randNum = random.randint(1,100)

    while guess != randNum:
        guess = input("Enter your guess: ")
        guessCount += 1

        if not isInteger(guess):
            print("Please enter a whole number.")

        elif int(guess) == randNum:
            print(f'Correct! You guessed the number in {guessCount} guesses!')
            break

        elif int(guess) > 100 or int(guess) < 1:
            print("Try a number between 1 and 100.")

        elif int(guess) > randNum:
            print("Try a little lower.")

        elif int(guess) < randNum:
            print("Try a little higher.")

    print("Would you like to play again? (Y/N)")
    yesNo = input().lower()
    guessCount = 0

    if yesNo.startswith("n"):
        break