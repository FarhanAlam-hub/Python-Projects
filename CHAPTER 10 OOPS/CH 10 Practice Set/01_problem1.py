class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p1 = programmer("Farhan",120000,823001)
p2 = programmer("Cizaan",100000,243001)
p3 = programmer("Hafeez",150000,892394)
print(p1.name,p1.salary,p1.pin,p1.company)
print(p2.name,p2.salary,p2.pin,p2.company)
print(p3.name,p3.salary,p3.pin,p3.company)