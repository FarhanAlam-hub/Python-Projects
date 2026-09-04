'''Question no.5 ---->Write a program to print the following RIGHT TRIANGLE pattern.
for n=3
*
**
***

'''
n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    print("*" * i,end="")
    print("")