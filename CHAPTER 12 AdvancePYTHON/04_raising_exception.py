a = int(input("Enter a: "))
b = int(input("Enter b: "))

if b == 0 :
    raise ZeroDivisionError("can't divide by zero")
else:
    print(f"Division is: {a/b}")

