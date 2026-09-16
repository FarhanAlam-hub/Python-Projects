age : int = 21 #---> this can be read as "age is expected to be an integer, and its value is 21."


def greeting(name:str) -> str: 
    return f"Hello,{name}"

print(greeting("Farhan"))
print(age)