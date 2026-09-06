def reverse(word):

    # l=word.split()
    # rl=[]

    # for i in range(len(l)):
    #     rl.append(l[len(l)-i-1])
    
    return " ".join(reversed(word.split()))

l1=input("Enter a sentence : ").lower()
print(reverse(l1))