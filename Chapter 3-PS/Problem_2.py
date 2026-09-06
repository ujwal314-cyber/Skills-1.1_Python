a=input("Enter your name : ")
b=input("Enter Date : ")
letter='''Dear <|Name|>
          You are selected !
          <|Date|>'''
print(letter.replace("<|Name|>",a).replace("<|Date|>",b))# the first replace function replaces the Name from the string stored in letter the second replace function replaces date  for the replaced one(name one)
# This is called as chaining