from math import sqrt
n=int(input("Enter a number : "))
l=[]
print("Enter the elements")
for i in range(n):
    e=int(input())
    l.append(e)

s=0
for i in l:
    s+=i
m=s/n
print("Mean is :",m)

v=0
for i in l:
    v=v+((i-m)**2)
v1=v/n
print("Variance is :",v1)

print("Standard Deviation is : ",sqrt(v1))