# We have to create a logic of calculating average using function ...
# INDIA'S GOT LATENT JUDGING SYSTEM
def avg():
    judge1 = float(input("Judge1 gives point: "))
    judge2 = float(input("Judge2 gives point: "))
    judge3 = float(input("Judge3 gives point: "))
    judge4 = float(input("Judge4 gives point: "))

    average = (judge1 + judge2 + judge3 + judge4) / 4
    print("Your's Average is: ",average)

avg()