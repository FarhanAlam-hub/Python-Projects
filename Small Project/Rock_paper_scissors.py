import random
items = ["rock","paper","scissors"]
computer = random.choice(items)
user=input("rock,paper,scissors: ").lower()
print("Computer chooses:",computer)
if user==computer:
    print("Match Draw")
elif user=="rock" and computer=="scissors":
    print("You win😍!!")
elif user=="scissors" and computer=="paper":
    print("You win😍!!")
elif user=="paper" and computer=="rock":
    print("You win😍!!")
else:
    print("You loose,Try again😭!!!")
