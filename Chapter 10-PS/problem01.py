class Programmer:
    company="Google"
    def __init__(self,name,lang,sal,add):
        self.name=name
        self.lang=lang
        self.sal=sal
        self.add=add
        print("Name :",self.name)
        print("Language :",self.lang)
        print("Salary :",self.sal)
        print("Address :",self.add)
h=Programmer("Harry","Java",1200000,"Delhi")