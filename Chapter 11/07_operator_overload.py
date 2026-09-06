# class Number():
#     def __init__(self, n):
#         self.n=n

# n=Number(2)
# m=Number(6)

# print(n+m) this prog would show an error as the operand type would not support therefore for this function overload is used


class Number():
    def __init__(self, n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n  # This is operator overload like this we can subtract multiply divide
    
    def __sub__(self,num):
        return self.n-num.n
    
    def __mul__(self,num):
        return self.n*num.n
    
    def __truediv__(self,num):
        return (self.n)/(num.n)
    
    def __floordiv__(self,num):
        return self.n//num.n
    
n=Number(36)
m=Number(6)

print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)