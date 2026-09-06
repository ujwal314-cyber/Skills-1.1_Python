# class Employee():
#     def __init__(self):
#         print("Constructor of Employee")
#     a=1
# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")
#     b=2
# class Manager(Programmer):
#     def __init__(self):
#         print("Constructor of Manager")
#     c=3

# r=Employee()
# print(r.a)
# h=Programmer()
# print(h.a,h.b)
# s=Manager()
# print(s.a,s.b,s.c)
# When you run this program  only the constructors of that particular class are run
# but if you want to run a constructor of a base class with that of the derived class then for that super is used

class Employee():
    def __init__(self):
        print("Constructor of Employee")
    a=1
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b=2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=3

r=Employee()
print(r.a)
h=Programmer()
print(h.a,h.b)
s=Manager()
print(s.a,s.b,s.c)