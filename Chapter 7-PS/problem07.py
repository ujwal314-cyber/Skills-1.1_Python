n=int(input("Enter a number : "))
for i in range(n+1):
    print(" "*(n-i),end="")# print by default gives a new line when you enter end=""it dorsnt give a new line
    print("*"*(2*i-1))