f=open("file.txt")
print(f.read())
f.close()
#the same can be written using with like this
with open("file.txt") as f:
    print(f.read())
# you do not need to close the file separately