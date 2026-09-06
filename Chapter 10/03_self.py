# class Employee:
#     lang="py" 
#     sal=1200000
#     def getInfo():
#         print(f"The salary is {sal} \nThe language is {lang}")

# harry=Employee()
# harry.getInfo()    "This would give an error as harry.getInfo() works same as Employee.grtInfo(harrry) but the  Employee function we have defined is Employee.getInfo() which does not take any argument hence it showed an erroe therefore we must declare an argument 'self' inside getInfo() or inside any functions we define inside a class to avoid such errors"
class Employee:
    lang="py" 
    sal=1200000
    def getInfo(self): # now this would work like Employee.getInfo(self)
        print(f"The salary is {self.sal} \nThe language is {self.lang}")

harry=Employee()
harry.lang="Java"
harry.getInfo() # This would be same as Employee.getInfo(harry)
print()
Employee.getInfo(harry)