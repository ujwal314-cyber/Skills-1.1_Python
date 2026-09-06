def great(a,b,c):
    if(a>b and a>c):
        print(f"{a} is gretest")
    elif(b>a and b>c):
        print(f"{b} is gretest")
    else:
        print(f"{c} is gretest")
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
great(a,b,c)