class employee():
    name = "Farhan"
    age = 21
    lang = "Python"
    salary = 1200000

    def getsalary(self):
        print(f"Your Salary is: {self.salary}")

    @staticmethod #----> WE USE @staticmethod when we don't take any value from the class attributes.   
    def greet():
        print("Good Morning")
farhan = employee()
farhan.greet()
farhan.getsalary()