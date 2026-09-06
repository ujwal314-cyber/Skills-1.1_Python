l=[1,4,7,8,5,4]

# lsq=[]
# for i in l:
#     lsq.append(i*i)
# this can be done easily using list comprehension

lsq=[i*i for i in l]

print(lsq)