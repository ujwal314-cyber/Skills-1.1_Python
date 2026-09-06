from functools import reduce
l=[2,4345,78654,34554,35,6356,789564]
def max(a,b):
    if a>b:
        return a
    return b
print(reduce(max,l))