if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements, expected <=3)")

# name =  input("Enter your name : ")
# print(name)
#  instead of writing this we can use walrus operator :=

print(name := input("Enter your name: ")) 