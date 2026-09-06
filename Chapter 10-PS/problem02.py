# class calc:
#     def sq(self):
#         print(self*self)
# n=int(input("Enter a number : "))
# n=calc()
# n.sq() #This would show an error to avoid this we must store n in something and then perform the operation
class calc:
    def __init__(self,n):
        self.n=n
    def sq(self):
        print(f"The square is {self.n*self.n}")
    def sqrt(self):
        print(f"The square root is {self.n**(1/2)}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
n=int(input("Enter a number : "))
n=calc(n)
n.sq()
n.sqrt()
n.cube()