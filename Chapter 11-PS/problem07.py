class vector:
    def __init__(self,l):
        self.l=l

    def __len__(self):
        return len(self.l)
    
a=vector([2,4,7])
print(len(a))