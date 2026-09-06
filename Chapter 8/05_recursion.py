def factorial(n):
    if(n==1 or n==0):# here the if condition is called the base condition as if this is not there then the recursion of the function would never stop
        return 1
    return n*factorial(n-1) # here the function keeps calling on itself until its value becomes 0 once 0 if condition gets executed and the factorial function at that time returns 1 then next it is substituted in n*1(where i is the return value of the fun) and the final value is returned
# here if the if was not there then the functtion would be executed infinitely and the program would crash
n=int(input("Enter a number "))
print(f"The factorial of {n} is {factorial(n)}")