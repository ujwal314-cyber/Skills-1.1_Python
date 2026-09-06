# class Employee():
#     sal=120000
#     def show(self):
#         print(f"Salary is  {self.sal}")

# harry=Employee()
# harry.sal=3000000
# harry.show()# this prog would print sal as 3000000 but you want to print class attribute so for that classmethod decorator is used


class Employee():
    sal=120000
    @classmethod
    def show(cls):
        print(f"Salary is  {cls.sal}")

harry=Employee()
harry.sal=3000000
harry.show()# as show is now defined as a class method the class attribute would be printed which is 1200000