try:
    n=int(input("Enter a Number : "))
    print(n)

except Exception as e:
    print(e)

else:# if try block is execued successfully then else block is executed
    print("I am inside else")

# else was required because if at all the statement was outside else then it would be executed even when there was an error