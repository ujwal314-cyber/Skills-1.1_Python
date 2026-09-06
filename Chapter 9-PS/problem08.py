with open("animal.txt") as f:
    content=f.read()
with open("copyanimal.txt","w") as f:
    f.write(content)