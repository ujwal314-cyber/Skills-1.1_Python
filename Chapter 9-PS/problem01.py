with open("p1_poem.txt") as f:
    content = f.read()
    if ("Twinkle" in content): # 'in is used to find whether the first is present in the second or not'
        print("Twinkle is present")
    else:
        print("Twinkle is not present")