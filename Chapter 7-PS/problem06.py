n=int(input("Enter a number : "))
s=1
i=1
while(i<=n):
    s*=i
    i+=1

print(f"Factorial of {n} is {s}")