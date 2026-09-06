a='gdjhg'
b="34536"
c='''dfg4647uj'''# all these are strings
d=len(a)# gives the length of the string 
print(d)

# Splicing
e="Harry" # the counting begins from 0 and goes 1 2 ... from last it will be like -1 -2 -3...
print(e[0:4])# starts from index 0 all the way till 4 excluding 4

print(e[:4])# means from beginning
print(e[3:])# means till last

# print(e[-1:-3]) is wrong 
print(e[-3:-1]) #is correct starts from -3 till -1 excluding -1

print(e[-1])
print(e[-4:]) # for printing even the last letter

# slicing with skip value

f="abcdefghijklmnopqrstuvwxyz"
print(f[3:10:4])# first resolves f[3:10] which will be 'defghijk' then it prints the first one then after d prints the 4th one then after that the 4th one of that then goes on