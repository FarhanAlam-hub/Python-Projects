a = 89 # ---> Global Variable

def fun():
    global a
    a = 3 #--> Local Variable
    print(a)

fun()
print(a)