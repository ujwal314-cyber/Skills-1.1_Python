# l=[2,56,89,656,46]
# index=0
# for i in l:
#     print(f"The number at index {index} is {i}")
#     index+=1

# the above prog can be simplified using enumerate

l=[2,56,89,656,46]
for index,i in enumerate(l):
    print(f"The number at index {index} is {i}")