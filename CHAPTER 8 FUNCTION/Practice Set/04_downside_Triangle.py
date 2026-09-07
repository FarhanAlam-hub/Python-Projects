def triangle(n):
    if n==0:
        return 
    print("*" * n)
    triangle(n-1)


n = int(input("Enter the value of n: "))
print(triangle(n))