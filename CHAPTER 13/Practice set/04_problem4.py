from functools import reduce

l = [232,4324,1213,565,7565,56453,7676,34,3423,21,354]

def greater(a,b):
    if (a>b):
        return a
    return b
print(reduce(greater,l))
