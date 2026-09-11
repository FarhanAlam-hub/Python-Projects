class Students:
    name = "Farhan"
    language = "Python"
    roll = 2430277

    def __init__(self,name,roll,language):   # dunder method which is automatically called
        self.name = name
        self.roll = roll
        self.language = language


    # def getroll(self):
    #     print(f"Your roll no. is:{self.roll}\nYour language is:{self.language} ")
    # def greet(self):
    #     print(f"Good moring, {self.name}")

farhan = Students("Farhan", 1224071,"JavaScript")
print(farhan.name,farhan.roll,farhan.language)
# farhan.greet()
# farhan.getroll()