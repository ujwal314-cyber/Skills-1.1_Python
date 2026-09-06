n=int(input("Enter a number : "))
a=0
for i in range(1,n+1):
    if(n%i==0):
        a+=1
if n==1:
    print("Neither Prime nor Composite")
elif a==2:
    print("Prime")
else :
    print("Composite")