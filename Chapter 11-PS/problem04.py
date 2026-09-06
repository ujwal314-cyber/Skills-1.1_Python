class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):
        return (self.r+c2.r,self.i+c2.i)
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
    
a=complex(2,4)
b=complex(6,7)
print(a+b)