class employee:
    def __init__(self,sal,inc):
        self.sal=sal
        self.inc=inc
    
    @property
    def salafterinc(self):
        return (self.sal + ((self.sal)*self.inc)/100)
    
    @salafterinc.setter
    def salafterinc(self,sal):
        self.inc=((sal/self.sal)-1)*100

harry=employee(234,20)
print(f"Salary is {harry.sal}")
print(f"Salary after increment is {harry.salafterinc}")
harry.salafterinc=280.8
print(f"Increment is {harry.inc}%")