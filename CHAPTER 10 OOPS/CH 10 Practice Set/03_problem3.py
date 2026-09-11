class demo:
    a = 4 # --> CLASS ATTRIBUTE

o = demo()

print(o.a) #--> this will print the class Attribute because instance attr is not present.

o.a = 0 # ---> INSTANCE ATTRIBUTE

print(o.a) # ---> This will print the instance attr because I.Attr is present.

print(demo.a) # ---> This will print the class Attribute

'''CONCLUSION ---> The Instance Attr. do not change the value of Class Attr.
The value of class attr remains same even if Instance attr is present.'''
