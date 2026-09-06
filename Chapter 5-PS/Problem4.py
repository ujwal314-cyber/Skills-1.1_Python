d={}
n=input("Enter your name : ")
l=input("Enter your favorite language : ")
d.update({n:l})
n=input("Enter your name : ")
l=input("Enter your favorite language : ")
d.update({n:l})
n=input("Enter your name : ")
l=input("Enter your favorite language : ")
d.update({n:l})
n=input("Enter your name : ")
l=input("Enter your favorite language : ")
d.update({n:l})
print(d)
#here if the same name is entered again then as the function is update the newly entered value will be assigned to that name
# for example if you enter ujwal then lang as python then next again you enter ujwal and c++ then c++ will be the value of ujwal
# but if you give the same values for different keys then it would be stored as entered only keys must be unique in dictionary