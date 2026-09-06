def strip(l,st):
    n=[]
    for i in l:
        if i!=st:
            n.append(i.strip(st))
    print(n)
    
l=["Rohan","Rahul","Mohan","Ram","an"]
st=input("Enter the string : ")
strip(l,st)