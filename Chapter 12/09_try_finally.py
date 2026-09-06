def final():
    try:
        n=int(input("Enter a Number : "))
        return n

    except Exception as e:
        print(e)

    finally:
        print("I am inside finally")
# when you return a value inside a function then once returned then the below statements would not be executed but when they are written inside finally then they would be executed even after returning 