# a function can also return a value if at all it is assigned to a variable
def sum():
    a=10
    b=20
    sum=a+b
    print(sum)

a=sum()
print(a)# the function will run but as it has no return value it will print None

def sum1():
    a=10
    b=20
    s=a+b
    print("sum  is", s)
    return s

b=sum1()
print(b)# here the function would be executed and also the value specified would be returned the return value can be anythig int float string bool