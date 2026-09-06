class demo:
    a=5

obj=demo()
print(obj.a)# prints class attribute as instance attribute is not set

obj.a=0 #Instance attribute is set

print(obj.a)#  prints instance attribute as instance attribute is set

print(demo.a)# The class attribute doesnt change