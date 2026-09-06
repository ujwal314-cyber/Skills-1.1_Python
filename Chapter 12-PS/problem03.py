n=int(input("Enter a number : "))

# l=[1,2,3,4,5,6,7,8,9,10]
# m=[f"{n} x {i} = {n*i}" for i in l]
# instead of this

m=[f"{n} x {i} = {n*i}" for i in range(1,11)]

print(m)

with open("multitable.txt","a") as f:
    f.write(f"Table of {n} is :\n\n")
    for i in m:
        f.write(f"{i}\n")
    f.write("\n")
    f.write("\n")