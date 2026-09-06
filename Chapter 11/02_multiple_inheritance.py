class Employee():
    company="ITC"
    def show(self):
        print((f"Name is {self.name} Salary is {self.sal}"))

class Coder():
    lang="Python"
    def showlang(self):
        print(f"Language is {self.lang}")

class Programmer(Employee,Coder):# Here Programmer is  derived from two parent classes so it contains attributes of both classes  
    company="ITC Infotech"# So programmer will contain all the statements defined  in both Employee and Coder
    def showcompany(self):
        print(f"Name is {self.name} Company is {self.company}")


harry=Programmer()
harry.name="Harry"
harry.sal=1200000
print(harry.company)
harry.show()
harry.showlang()
harry.showcompany()