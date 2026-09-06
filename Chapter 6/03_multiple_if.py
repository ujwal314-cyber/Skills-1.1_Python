a=int(input("Enter your age : "))

# if statement 1
if a%2==0:
    print("Even")
 # if statement 2
if a>=18:
    print("Major")
elif a<0:
    print("Age cannot be negative please enter a valid age")
elif a==0:
    print("Age cannot be 0 please enter a valid age")
else:
    print("Minor")
# end of if statement 2

# if statement can exist independently without else but elif and else cannot exist without if

# there can be n number of elif statements bw if and else