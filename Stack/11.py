import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Enter a number (1-100): "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! You guessed it.")
        break