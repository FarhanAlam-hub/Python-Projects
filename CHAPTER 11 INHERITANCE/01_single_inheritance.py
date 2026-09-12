class Employee: # ----> BASE CLASS / PARENT CLASS
    company = "ITC"

class programmer(Employee): # --->  DERIVED CLASS / INHERITED CLASS
    company = "ITC_Infotech"

a = Employee()
b = programmer()

print(a.company,b.company)
