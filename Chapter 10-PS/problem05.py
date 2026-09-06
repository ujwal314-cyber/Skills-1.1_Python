from random import randint

class train:
    def __init__(self,trno):
        self.trno=trno
    
    def bookt(self,fro,to):
        print(f"Your ticket is booked for train no {self.trno} from {fro} to {to}")

    def status(self):
        print(f"Your train {self.trno} is running on time")

    def fare(self,fro,to):
        print(f"Your ticket fare for train {self.trno} from {fro} to {to} is {randint(100,200)}")

pass1=train(2578)
pass1.bookt("Delhi","Pune")
pass1.status()
pass1.fare("Delhi","Pune")