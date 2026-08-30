a = float(input("Enter your Balance : "))


if (a % 100 != 0):
    print("Insufficient Balance: :(")
elif(a%100==0):
    w = float(input("Enter the amount you want to withdraw:"))

print("Your remaining balance is: ", a-w)