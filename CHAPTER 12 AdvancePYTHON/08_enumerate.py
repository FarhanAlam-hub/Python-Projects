l = [2,3,4,1,10]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
     print(f"The item number at index {index} is {item}")