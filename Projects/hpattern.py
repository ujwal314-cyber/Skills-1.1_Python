n=int(input())

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("H"*((2*i)-1))

o=int((n+1)/2)

for i in range(1,n+2):
    print(" "*(o-1),end="")
    print("H"*n,end="")
    print(" "*(3*n),end="")
    print("H"*n)

for i in range(1,o+1):
    print(" "*(o-1),end="")
    print("H"*(n*5))

for i in range(1,n+2):
    print(" "*(o-1),end="")
    print("H"*n,end="")
    print(" "*(3*n),end="")
    print("H"*n)

c=0

for i in range(n,0,-1):
    print(" "*((4*n)+c),end="")
    print("H"*((2*i)-1))
    c+=1