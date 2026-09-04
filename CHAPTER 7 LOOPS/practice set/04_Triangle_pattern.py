''' ****Question no. 4 Write a program to print the following star Triangle pattern.

  *
 ***
*****

'''
n = int(input("Enter the value of n:"))

for i in range(1, n+1):
        print(" " * (n-i),end="")
        print("*" * (2*i-1),end="")
        print(" ")
