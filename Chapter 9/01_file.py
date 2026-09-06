f= open("file.txt")# opens the file
d=f.read()# reads the file opened in f and the data in it is assigned to d
print(d)#prints the data stored in d
f.close()# closes the file opened in f so that it can be accessed somewhere else 