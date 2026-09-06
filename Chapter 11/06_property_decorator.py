class Employee():
    @property
    def name(self):# the getter takes only one argument which is self
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value): # the function names of both getter and setter should be of the same name
        self.fname=value.split(" ")[0]# Splits and stores the the element of the list of the specified index
        self.lname=value.split(" ")[1]
# here u are not telling the user to enter the first name and last name separately instead ypur are telling the user to enter full name and using the full name you are extracting first and last name
# this the function of property and setters where you take a value from user and you perform some functions on them like the above
harry=Employee()
harry.name="Harry Khan" # Here the "Harry Khan" becomes the value of the setter
print(harry.name)
print(harry.fname)
print(harry.lname)

varun=Employee()
varun.name="Varun Reddy"
print(varun.name)
print(varun.fname)
print(varun.lname)