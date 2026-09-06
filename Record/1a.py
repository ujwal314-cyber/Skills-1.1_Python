a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

c=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter your choice : "))

if(c==1):
    print(a+b)

elif(c==2):
    print(a-b)

elif(c==3):
    print(a*b)

elif(c==4):
    print(a/b)
    
else:
    print("Please enter a number from 1 to 4")