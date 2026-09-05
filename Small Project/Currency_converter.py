'''CURRENCY CONVERTER'''

amount = float(input("Enter the amount in ₹ : "))

print ("1. INR to USD")
print ("2. INR to EUR")
print ("3. INR to GBP")

choice = int(input("Enter your choice: "))

if choice == 1:
    usd = amount / 95
    print("USD:",usd)

elif choice == 2:
    eur = amount / 110
    print("Euro: ",eur)

elif choice == 3:
    gbp = amount / 128
    print("GBP: ",gbp)

else:
    print("Invalid Choice!!!")