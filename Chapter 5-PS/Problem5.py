# s={1,2,4,6,9,[1,3]}    # you cannot have a list inside a set as it is mutable and sets  are supposed to contain only the elements which are immutable
# so the above one would show an error but a set can contain a tuple as they are immutable
s={1,2,4,6,9,(1,3)}
print(s)