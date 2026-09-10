class Students:
    name = "Farhan"
    language = "Python"
    roll = 2430277
    def getroll(self):
        print(f"Your roll no. is:{self.roll}\nYour language is:{self.language} ")
    def greet(self):
        print(f"Good moring, {self.name}")

farhan = Students()
farhan.greet()
farhan.getroll()
# print(farhan.name,farhan.roll)