# Map Example
l=[1,2,3,4,5]

sq=lambda x:x*x

sqlist=map(sq,l)# maping a function for list of items

print(list(sqlist)) 


# Filter Example
def even(n):
    if(n%2==0):
        return True
    return False

evenlist=filter(even,l)# filters the given list based on the given function
print(list(evenlist))

# Reduce Example
from functools import reduce
sum=lambda a,b:a+b
# the above lambda function would work same as 
# def sum(a,b):
#     return a+b

print(reduce(sum,l))

# reduce function would work like 
# here list = 1,2,3,4,5
# 1 + 2 3 4 5
#   3 + 3 4 5
#     6 + 4 5
#      10 + 5
#         15 which is the output
# subtraction multiplication and division or other operations would also work in the same way