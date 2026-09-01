mass = float(input("Enter your weight: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your Age: "))
gender = input("Enter your Gender: ")
height = height / 100
bmi = mass/(height**2)
print("Your Body mass Index (BMI) is: ",bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

