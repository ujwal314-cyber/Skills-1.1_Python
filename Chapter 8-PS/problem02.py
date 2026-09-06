def ctof(c):
    f=((9/5)*c)+32
    return f
c=float(input("Enter temperature in celcius : "))
print(f"{ctof(c)} degree farenheit")