'''Question no.6 ---->Write a program to print the following RECTANGLE pattern.
for n=3
***
* *
***

'''
n= int(input("Enter the value of n:"))
for i in range(1,n+1):
    if (i==1 or i==n):
        print("*" * n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")