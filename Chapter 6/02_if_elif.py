a=int(input("Enter your age : "))
 # if elif ladder
if a>=18:
    print("Major")
elif a<0:
    print("Age cannot be negative please enter a valid age")
elif a==0:
    print("Age cannot be 0 please enter a valid age")
else:
    print("Minor")