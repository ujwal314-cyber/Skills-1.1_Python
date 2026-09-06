words=["donkey","monkey","dog","buffalo"]
with open("animal.txt","r") as f:
    content=f.read()
    content=content.lower()
    for i in words:
        if i in content:
            content=content.replace(i,"#"*len(i))
            with open("animal.txt","w") as f:
                f.write(content)