s=set()
s.add(18)
s.add("18")
print(s)# here it two types of datatypes therefore the set stores both the values
#but
s1=set()
s1.add(18)
s1.add(18.0)
s1.add('18')
print(s1)# here the set will contain 18 and '18' but doesnt contain 18.0 because python compares the values first and then checks the data type as 18==18.0 returns true it doesnt store 18.0 as aready 18 is there
# based on what is added first it dispayes that in the set like here 18 is added before 18.0 hence it contains 18 and there is no 18.0 but if 18.0 was added first then it would have contined 18.0 instead of 18