with open("log.txt") as f:
    content=f.read()
    if "python"or"Python"or"PYTHON" in content:
        print("Pyhton is present")
    else:
        print("Not present")