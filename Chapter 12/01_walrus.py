if (n:=len([1,2,3,4,5,6,7])) >3:
    print(f"Your list is too long ({n} elements , expected <=3)")
    # here walrus operator does two operations one assigns len of list to n and checks whether n> 3 or not
    # if this done without walrus then it would be
    # n=len([1,2,3,4,5,6,7])
    # if n>3: