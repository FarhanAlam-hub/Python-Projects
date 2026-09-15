class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r , self.i + c2.i)

    def __mul__(self, c2):
            real = self.r * c2.r - self.i * c2.i
            imaginary = self.r * c2.i + self.i * c2.r
            return Complex(real,imaginary)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(5,4)
c2 = Complex(2,3)

print(c1 + c2)
print(c1 * c2)