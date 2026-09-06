class Employee:
    lang="py"
    sal=1200000
    # def __init__(self): # anything which is written within double underscores is called a dundder which is called automatically when class employee is called
    #    print("HEllo") and a self argument must be given otherwise it would show an error

    def __init__(self,name,sal,lang): # here init is called a constructer
        self.name=name
        self.sal=sal
        self.lang=lang
  
harry=Employee("Harry",1200000,"Java")
print(harry.name,harry.sal,harry.lang)

# Rohan=Employee() # as a dunder is automatically called if at all any arguments are defined inside the dunder they mst be given a value when the class is called othervise it would show an error
# print(Rohan.name,Rohan.sal,Rohan.lang)

rohan=Employee("Rohan",1600000,"C++")
print(rohan.name,rohan.sal,rohan.lang)