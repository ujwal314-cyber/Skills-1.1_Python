with open("animal.txt") as f:
    content=f.read()
with open("copyanimal.txt") as f:
    content2=f.read()
if(content==content2):
    print("Both the files are identical")
else:
    print("Both the files are not identical")