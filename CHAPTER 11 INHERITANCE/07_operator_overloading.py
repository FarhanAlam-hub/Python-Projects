class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    def __truediv__(self, num):
            return self.n / num.n

    def __floordiv__(self, num):
                return self.n // num.n
    

n = number(6)
m = number(2)

print(f"The sum is: {n + m}")
print(f"The difference is: {n - m}")
print(f"The product is: {n * m}")
print(f"The division is: {n / m}")
print(f"The floor_Division is: {n // m}")