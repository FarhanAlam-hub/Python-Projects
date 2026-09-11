class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is:{self.n**2}")

    def cube(self):
        print(f"The cube is:{self.n**3}")

    def squareroot(self):
        print(f"The square is:{self.n**1/2}")
n = int(input("Enter the value of n: "))
a = calculator(n)
a.square()
a.cube()
a.squareroot()