f=open("file.txt")
l=f.readlines() # this creates a list of the lines in the opened file
print(l)
print(type(l))
f.close()
f=open("file.txt")# for performing each function the file should be opened newly
print(f.readline())# readline() function reads the lines in the file one by one
print(f.readline())
print(f.readline())
print((f.readline())=="")# in file.txt there are only three lines but here there are four readline statements so the last statement returns an empty string
print()
# the above task of  printing each line in the file can be done using loop
f=open("file.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()