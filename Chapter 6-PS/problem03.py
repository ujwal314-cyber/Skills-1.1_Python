message=input("Enter your comment")
s1="Make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"
if(s1 in message or s2 in message or s3 in message or s4 in message):
    print("This is a spam")
else :
    print("This is not a spam")
#here in checks whether the specified string is there in the message or not