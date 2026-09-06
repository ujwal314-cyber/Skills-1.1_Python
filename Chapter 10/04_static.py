class Employee:
    lang="py" 
    sal=1200000
    def getInfo(self):
        print(f"The salary is {self.sal} \nThe language is {self.lang}")

    # def greet(self): This does not take any object but also we must declare one inside it as it would show an error without it so to avoid declaring one argument for those functions which do not take one @staticmethod is used like
    #     print("Good Morning")
    
    @staticmethod # this is a decorator
    def greet():
        print("Goog Morning")


harry=Employee()
harry.getInfo()  
harry.greet()