word="donkey"
with open("donkey.txt","r") as f:
    content=f.read()
    content=content.lower()
    if word in content:
        content=content.replace("donkey","######")
        with open("donkey.txt","w") as f:
            f.write(content)
    else:
        print("There is no donkey word in your sentence")