def great(a,b,c):
    if a > b and a > c:
        print(f"{a} is greatest!!")
    elif b > a and b > c:
        print(f"{b} is greatest!!")
    elif c > a and c > b:
        print(f"{c} is greatest!!")

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

great(a,b,c)

    