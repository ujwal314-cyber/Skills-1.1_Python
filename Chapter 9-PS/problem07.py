with open("log.txt") as f:
    content=f.readlines()
    for i in content:
        if ("python" in i):
            print(f"Python is present in line {(content.index(i))+1}")
            break
    else:
        print("Pyhton is not present")