# Question No.1 ----->Write a program to greet all the person names stored in a list 'l' and which starts
#with F.
l =["Farhan","Faizan","Cizaan","Fatima","Kaif"]

for name in l:
    if(name.startswith("F")):
        print("Hello ",name)