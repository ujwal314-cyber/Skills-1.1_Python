from datetime import datetime
n=input("Enter your name : ")
byr=int(input("Enter your birth year : "))
cyr=datetime.now().year
age=cyr-byr
print(f"{byr}\n{cyr}\n{age}")
if(age>=60):
    print(n,"is a senior citizen")
else:
    print(n,"is not a senior citizen")