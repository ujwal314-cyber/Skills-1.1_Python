a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
try:
    print(a/b)

except ZeroDivisionError as z:
    print("Infinite")
    print(z)