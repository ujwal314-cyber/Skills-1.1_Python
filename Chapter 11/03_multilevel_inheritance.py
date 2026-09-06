class Employee():# Parent class
    a=1
class Programmer(Employee):# Derived from Employee
    b=2
class Manager(Programmer):# Derived from Programmer
    c=3

r=Employee()# cannotprint b and c
print(r.a)
h=Programmer()# can print a also as it is derived from Employee but cannot print c
print(h.a,h.b)
s=Manager()# can print all a b c as it is derived from Programmer which is inturn derived from Employee
print(s.a,s.b,s.c)