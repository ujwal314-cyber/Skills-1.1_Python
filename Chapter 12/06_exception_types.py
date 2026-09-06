try:
    n=int(input("Enter a Number : "))
    print(n)

except ValueError as v:# you can print different messages for different types of errors like here entering str instead of int is a value error so that particular statements would be executed if other types of error then the exception would be executed
    print("heyy")
    print(v)

except Exception as e:
    print(e)

print("Thank You")