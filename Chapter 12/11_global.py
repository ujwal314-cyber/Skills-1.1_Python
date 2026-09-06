# a=43# here a is a global variable which means it can be used anywhere in the program

# def fun():
#     a=7 # here a is a local variable which means it can be used only inside this particular function
#     print(a)

# print(a)
# fun()
# the above prog would print 43 
                          #  7

a=43

def fun():
    global a # this keyword would make the local variable a a global variable
    a=7 
    print(a)

# print(a)
# fun() This would also give the same output as the before one as here fun() is called after printing due to which the a=7 is declared global after printing a==43

fun()
print(a)# this would give both a's as 7 as now before printing a a=7 is declared as global so the new value of a=43 is 7 if at all after calling fun() another value is assigned to a then that new value would be printed in the print statemnt but not in the fun()