import random

computer = random.randint(1,100)

while True:
    user = int(input("Guess the number between (1-100): "))

    if user<computer:
        print("Too low!!!")
    elif user > computer:
        print("Too High!!!")
    else:
        print("Correct! You Won🎉")
        break