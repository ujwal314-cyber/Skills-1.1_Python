filename=input("Enter file name : ")
with open(filename,'r') as f:
    cont=f.read()

words=cont.lower().split()

freq={}

for word in words:
    word=word.strip(",.'/\"(){}[]")

    freq[word]=0

for i,j in freq.items():
    if i:
        freq[word]=j+1

sort=sorted(freq.items(),key=lambda x:x[1],reverse=True)

print("Top 10 words are : ")
for i,j in sort[:10]:
    print(i,"-",j)