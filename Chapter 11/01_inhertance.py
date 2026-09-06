class Employee():
    company="ITC"
    def show(self):
        print((f"Name is {self.name} Salary is {self.sal}"))

# class Programmer():
#     company="ITC Infotech"
#     def show(self):
#         print(f"Name is{self.name} Salary is {self.sal}")

# # Here the first statements are ssame as class employee therefore this class can be made as a inherited class and there will be no need to type the repeated statements again in inherited class

#     def showlang(self):
#         print(f"Name is{self.name} Language is {self.lang}")
# The above statements can be written in a shorter way using inheritance

class Programmer(Employee): # Here Programmer is a inherited or a child class and employee is a parent calss
    company="ITC Infotech" # Here Employee is a base class and Programmer is a derived class
    def showlang(self):
        print(f"Name is {self.name} Language is {self.lang}")

a=Employee()
b=Programmer()
print(a.company,b.company)

harry=Programmer()
harry.name="Harry"
harry.sal=1200000
harry.lang="Py"
print(harry.company)
harry.show()
harry.showlang()