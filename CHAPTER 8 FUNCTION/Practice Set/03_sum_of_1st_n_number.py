def sum(n):
    if n==1:
        return 1
    else: 
        return sum(n-1)+n


n = int(input("Enter the value of n: "))
print(f"The sum of fist n natural number is: {sum(n)}")