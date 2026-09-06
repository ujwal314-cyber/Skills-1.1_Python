a :int = 23
b: str="sjvhf" # you can mark the variable with its type so that when another user uses your code he gets to know what type of variable it is

def sum(c:int,d:int) -> int :# so when you mark a function like this , when the function is called it would show the type of variables to be given to the function and its return type
    return c+d

sum(5,6)

# in the same way if you want to to mark a list tuple dict you must import a module
from types import List , Dict ,Tuple ,Union

l1: List[int] =[1,2,3,4,5,6]# This tells that this is a list of integers
d1: Dict[str,int] = {"a":1,"b":2}# this tells that the key value pairs in the dict are str:int
t1: Tuple[float,int] = (1.6,4)# this tells that this is a tuple of two which are float and int
un: Union[int,str]="1jnh3446"# this tells that the variable is a union of int and string
# a union is basically a variable that can hold multiple types