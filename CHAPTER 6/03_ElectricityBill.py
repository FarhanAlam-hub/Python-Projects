unit = int(input("Enter the unit you used:"))
if (unit<100):
    print("Your bill is:" ,(unit*5))
elif(unit<0):
    print("invalid unit:")
elif (unit>100 and unit<200):
    print("Your bill is:" ,(unit*7))
elif (unit>200 and unit<300):
    print("Your bill is:", (unit*10))
else:
    print("Your bill is:" ,(unit*15))

print("done:")