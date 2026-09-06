class D2:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j")

class D3(D2):
    def __init__(self,i,j,k):
        super ().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")

a=D2(4,5)
a.show()
b=D3(6,8,4)
b.show()