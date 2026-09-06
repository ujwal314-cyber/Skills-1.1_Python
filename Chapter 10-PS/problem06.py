from random import randint

class train:
    def __init__(slf,trno):
        slf.trno=trno
    
    def bookt(slf,fro,to):
        print(f"Your ticket is booked for train no {slf.trno} from {fro} to {to}")

    def status(slf):
        print(f"Your train {slf.trno} is running on time")

    def fare(slf,fro,to):
        print(f"Your ticket fare for train {slf.trno} from {fro} to {to} is {randint(100,200)}")

pass1=train(2578)
pass1.bookt("Delhi","Pune")
pass1.status()
pass1.fare("Delhi","Pune")

# instead of self slf or harry or anything can be used the program would be executed but using self would increase the readability of the program