marks={"Rohan":100,"Harry":95,"Pavan":86}
print(marks.items())#lists the elements of the dict in (key,value) tuple form
print(marks.keys())# prints all the keys in the dictionary
print(marks.values())# prints all the values in the dictionary
marks.update({"Rohan":98,96:"Ramesh"})# updates a existing value or adds a new value at the end of the dict
print(marks)
print(marks.get("Pavan"))
print(marks.get("Harish"))# the difference bw this and the below one is that if you ask to print the value of a key which doesnt exist in the dict the get function returns none but the [] returns an error
# print(marks["Harish"])
print(marks.pop(96))# Removes the specified key and its value and returns its value
print(marks)
print(marks.popitem())# Removes the last key of the dictionary and its value and returns both key and its value
print(marks)
marks.clear()#clears the entire dictionary
print(marks)
print(len(marks))# len function can be used to find the length of anything