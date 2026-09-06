s1={2,1,5,8,12,14,20}
s2={2,4,5}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)
print({1,2}.issubset(s1))
print(s1.issuperset({2,1}))
print(s1.difference(s2))# is basically s1-s2
print(s2.difference(s1))# is basically s2-s1