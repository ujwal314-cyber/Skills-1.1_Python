l1=[2,56,90,9.03,89]
print(l1.sort())# sorts the list in increaing order
print(l1)
print(l1.reverse())# reverses the order of the list
print(l1)
print(l1.append(77))# adds the given element at the end of the list
print(l1)
print(l1.insert(5,"Hello"))# inserts the given element such that its index would be the specified one here 5
print(l1)
print(l1.remove(90))# removes the specified element from the list
print(l1)
print(l1.pop(4))# removes the element at the specified index and returns its value , if the list is printed after this function the it would not contain the specified element
print(l1)
# Here the list methods though they are inside the print function the list has under gone all the methods in the given order
# for example first is sort the list would have been sorted then reverse the sorted list would be reversed then next one like this
l1.sort()# sort functions sorts only int and float if a string comes in between it does not sort the numbers present after the string
l1.reverse()
print("all combined ",l1)
# only pop returns a  value hence it is printed others dont return a value hence it is showing none