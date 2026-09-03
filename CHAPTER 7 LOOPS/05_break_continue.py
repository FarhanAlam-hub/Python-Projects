#           *******BREAK Statement(used to come out from loop)********
print("THIS IS THE O/P OF BREAK!!!")
for i in range(2,21,2):
    if i == 10:
        break
    print(i)


#******CONTINUE Statement(used to stop the current iteration and continue to next within the loop)*****
print("THIS IS THE O/P OF CONTINUE!!!")
for i in range (5):
    if i == 3:
        continue
    print(i)