# as a tuple is not mutable like a string so when you use a method on a tuple always a new tuple is created the original tuple remains the same 
t=(13,25,6,32,"ljhg",3.98)
print(t.count(32))# counts the number of times the specified element is repeaed in the tuple
print(t.index(32))# gives the index of the specified element in the tuple

t2=t+(25,78,90)# concardinates two tuples
print(t2)

print(t*3)# the tuple is repeated the specified number of times

print(2 in t)# checks whether the specifiedd element is present in the tuple or not
print(13 in t)

print(len(t))