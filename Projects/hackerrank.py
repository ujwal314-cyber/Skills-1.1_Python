from functools import reduce
r=int(input())

l=list(input())    
    

def max(a,b):
    if a>b:
        return a
    return b
    
print(reduce(max,l))