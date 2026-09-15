class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Two vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
            print(f"The Three vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(5,2)
a.show()
b = ThreeDvector(4,2,3)
b.show()