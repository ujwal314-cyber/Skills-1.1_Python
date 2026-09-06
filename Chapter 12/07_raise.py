a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

if(b==0):
    raise ZeroDivisionError ("Hey this program is not meant for dividing numbers with zero")# raising a error would cause the prog to crash 

else : 
    print(f"a/b is {a/b}")