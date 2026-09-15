class employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterincrement(self):
        return (self.salary + self.salary * (self.increment/100))

# new salary = old salary (1 + increment/100)

    @salaryAfterincrement.setter
    def salaryAfterincrement(self, salary):
        self.increment = ((salary / self.salary) - 1 )*100

e = employee()
print(e.salaryAfterincrement)
e.salaryAfterincrement = 280.8
print(e.increment)