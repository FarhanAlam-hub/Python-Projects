#WAP to convert the inches in centimeters.....

def length(n):
    return n * 2.54

n = int(input("Enter the length in inches: "))
print(f"The length in cms is: {length(n)}")