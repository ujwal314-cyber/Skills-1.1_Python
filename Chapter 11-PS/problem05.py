class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,n):
        return vector(self.x+n.x,self.y+n.y,self.z+n.z)
    
    def __mul__(self,n):
        return ((self.x*n.x)+(self.y*n.y)+self.z*n.z)
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
a=vector(4,5,6)
b=vector(6,5,4)
print(a+b)
print(a*b)