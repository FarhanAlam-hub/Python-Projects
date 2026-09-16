import random

n = random.randint(1,100)
a = -1
guesses = 0
while (a != n):
    a = int(input("Guess the number between (1-100): "))

    if a>n:
        print("Lower number please!!!")
    elif(a<n):
        print("Higher number please!!!")
    guesses += 1
    
print(f"You Guess the number {n} correctly in {guesses} attempts🎉")