class vehicles:
    vehicles = "Four Wheeler"

class cars(vehicles):
    cars = "BMW"

class bike(cars):
    bike = "Bullet"

a = vehicles()
b = bike()

print(a.vehicles,b.cars,b.bike)