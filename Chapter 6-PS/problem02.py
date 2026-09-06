p=int(input("Enter marks in physics : "))
c=int(input("Enter marks in chemistry : "))
m=int(input("Enter marks in maths : "))
if((p+c+m)/300)>=0.4:
    if (p/100 >=0.33 and c/100 >=0.33 and m/100 >=0.33):
        print("Pass")
    else : print("Fail")
else :
    print("Fail")