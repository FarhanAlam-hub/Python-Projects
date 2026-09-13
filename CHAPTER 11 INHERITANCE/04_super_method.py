class vehicles:
    def __init__(self):
        print("This is the constuctor of vehicles class")
    vehicles = "Four Wheeler"

class cars(vehicles):
    def __init__(self):
        super().__init__()
        print("This is the constuctor of cars class")
    cars = "BMW"

class bike(cars):
    def __init__(self):
        super().__init__()
        print("This is the constuctor of bike class")
    bike = "Bullet"

# a = vehicles()
# print(a.vehicles)

# b = cars()
# print(b.cars)

c = bike()
print(c.bike)
