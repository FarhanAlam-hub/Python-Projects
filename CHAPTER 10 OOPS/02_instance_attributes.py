class Students:
    name = "Farhan"
    language = "Python" # ------> Class Attributes
    roll = 240277

farhan = Students()
farhan.language = "JavaScript"   # ------> Instance Attribute is more powerfull than class Attributes
print(farhan.name,farhan.roll,farhan.language)