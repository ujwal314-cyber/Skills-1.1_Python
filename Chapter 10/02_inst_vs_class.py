class Employee:
    lang="py" 
    sal=1200000

harry=Employee()
harry.lang="Java" 
print(harry.sal,harry.lang)# java is printed instead of py as instance takes preference over class attributes
# First it checks whether instance is present if not there then it goes for class attribute