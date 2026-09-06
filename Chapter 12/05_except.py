try:
    n=int(input("Enter a Number : "))# if this statement was outside try and except anf if at all the user enters a string instead of a integer value then the program would crash and no other statements below it would be executed but if this was inside try then it would still show an error but the program would not crash and the below statements would still be executed
    print(n)

except Exception as e:# if the user enters astring instead of int then only this except block would run otherwise not
    print(e)

print("Thank You")