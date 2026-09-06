a="ujwal"
print(len(a))# prints the length of a
print(a.endswith("al"))# returns true or false based on the ending of the string 
print(a.startswith("U"))# returns true or false based on the starting of the string
print(a.count("w"))# counts the number of times the given alphabet is repeated in the string 
print(a.capitalize())# capitalizes the first letter of the string
print(a.find("wal"))#finds the location of the given letter of set of letters in the string if not found returns -1
print(a.replace("wal","ju"))#replaces the all the occurances of thr first set with the second
print(a.upper())# converts the entire string into upper case
print(a.lower())# converts the entire string into lower case
print("hello world".title())# capitalizes the starting letter of each word in the string
print(" hello world ".strip())# strips the starting and trailing spaces in the string
print(" hello world ".rstrip())# strips the trailing spaces in the string
print("Amir Khan".split(" "))# Splits the string at the specified string in split and makes a list of them
print("Amir Khan".split("i"))
s="Rohan".strip("an")
print(s)