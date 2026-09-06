st="I am amazing"
f=open("myfile.txt","w")# open function takes two arguments one is the file name other the mode in which it should open the file "r" rstands for read mode which is the default mode of this function
# another mode is "w" which is write mode 
f.write(st)# this function writes the entered value in the file

f.close()