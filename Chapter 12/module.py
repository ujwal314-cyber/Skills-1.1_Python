def func():
    print("Hello World")

# print(__name__)# This would print __main__ if this is executed in the file in which is created if this is imported and executed then it would show module

if (__name__) == ("__main__"):
    print("This in executed in the main file")
    func()

else:
    print("This is executed in another file")

print("Hello there")