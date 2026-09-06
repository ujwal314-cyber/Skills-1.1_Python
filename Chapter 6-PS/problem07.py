post=input("Enter the post : ")
you=input("Enter your name : ")
# if you in post:# This has a problem that if the post and name are in different cases then it wont work
#     print("The post is talking about you")
if you.lower() in post.lower():
    print("The post is talking about you")
else:
    print("The post is not talking about you")