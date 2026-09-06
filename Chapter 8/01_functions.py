def percent(): # function definition, a function contains a set of statements which get executed when you call the function
    n=int(input("Enter the number of subjects for which you want to calculate the percentage : "))
    s=0
    denominator=n*100
    for i in range(1,n+1):
        a=int(input(f"Enter marks of subject {i} : "))
        s=s+a
    percentage=(s/denominator)*100
    print("Percentage is",percentage)

percent() # function call , when a function is called all the statements in it are executed
# a function can be called n number of times in a program

#here percent is a user defined function 
# there is one more type of function which is built in functions which are for example print(), len(), etc