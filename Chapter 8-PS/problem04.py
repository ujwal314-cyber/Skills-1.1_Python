def pattern(n):
    if(n==0):
        return # if return is executed then the statements after it are not called
    print("*"*n)
    pattern(n-1)
 

pattern(5)