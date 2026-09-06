class Employee:
    lang="py" # here lang and sal are class attributes
    sal=1200000

harry=Employee()
harry.name="Harry" # here name is a instance attribute
print(harry.name,harry.sal,harry.lang)

# Name is a instance attribute(object attribute) and belongs only to that object
# But sal and lang are class attributes and belongs to class and all the objects to which the class is assigned to 

rohan=Employee()
rohan.name="Rohan"
print(rohan.name,rohan.lang,rohan.sal)
# here class acts as a noun
#like 
# Noun > class > Employee
#Adjective > Attributes > name,lang,sal
#Verbs > Methods > increment()