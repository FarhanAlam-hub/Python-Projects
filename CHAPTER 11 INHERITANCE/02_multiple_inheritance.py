class Employee: # ----> 1st BASE CLASS / PARENT CLASS
    company = "ITC"

class coder:   # ----> 2nd BASE CLASS / PARENT CLASS
    language = "Python"

class programmer(Employee,coder): # --->  DERIVED CLASS / INHERITED CLASS
    company = "ITC_Infotech"

a = Employee()
b = programmer()

print(a.company,b.company,b.language)