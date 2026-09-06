md=input("Enter a mnultidigit number : ")
l=[0]*10

for i in md:
    if i.isdigit():
        d=int(i)
        l[d]=l[d]+1

for i in range(10):
    print(i,"-",l[i])