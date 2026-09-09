# Check weather the number is Even or odd..

n = int(input("Enter the number: "))

if n % 2 == 0:
    print(f"{n} is Even!!!")
elif n == 1:
    print(f"{n} Neither Even Nor Odd!!!") 
else:
    print(f"{n} is odd!!!")