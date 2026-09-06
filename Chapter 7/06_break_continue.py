for i in range(100):
    if(i==20):
        break # exits the loop  right now
    print(i)

print()

for i in range(100):
    if(i==20):
        continue # skips the iteration means the loop executes till i = 20 when i will be 20 the continue will be executed and the statements below continue will not be executed for the iteration and it will go for a new iteration
    print(i)