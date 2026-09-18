def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = [5,12,43,45,12345,32,54,40,20,21]

f = list(filter(divisible5,a))
print(f)