def gentables(n):
    table=""
    for i in range(1,11):
        table+=f"{n} x {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:# open function can create new files but cannot create new folders so you must first create tables first and then the table_n files are created on their own
        f.write(table)
for i in range(1,21):
    gentables(i)