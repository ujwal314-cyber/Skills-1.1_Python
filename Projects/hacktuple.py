n=int(input())

l=input()

t=tuple()

for i in l:
    if i!=" ":

        x=tuple(i)
        t=t+x
    
t=tuple(map(int,t))

print(t)

print(hash(t))