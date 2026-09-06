from random import randint

number=randint(1,100)
i=0
while True:
    while True:
        guess= int(input("Guess the number from 1 to 100 : "))
        i=i+1
        if(guess==number):
            print("Your guess is correct")
            break
        elif(guess>number):
            print("Lower number please")
        elif(guess<number):
            print("Higher number please")
        else :
            print("Enter a number please")
    print(f"You took {i} guesses to guess the correct number")
    c=input("Do you want to continue the game type Yes/No : ")
    c=c.lower()
    if(c=="yes"):
        continue
    elif(c=="no"):
        print("Thank You")
        break
    else:
        print("Please enter Yes or No : ")
        break