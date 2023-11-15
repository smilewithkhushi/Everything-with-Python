#calculator program

def takeInput():
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    return a,b

def addition(x,y):
    add=x+y
    print("The sum of two numbers is : ", add)
    return add

def subtraction(x,y):
    sub=x-y
    print("The difference of two numbers is : ", sub)
    return sub

def multiply(x,y):
    mul=x*y
    print("The product of two numbers is : ", mul)
    return mul

def division(x,y):
    div=x/y
    print("The division of two numbers is : ", div)
    return div

def floorDivision(x,y):
    fd=x//y
    print("The Floor Division of two numbers is : ", fd)
    return fd

def modulus(x,y):
    rem=x%y
    print("The Remainder from Division of two numbers is : ", rem)
    return rem

def power(x,y):
    pow=x**y
    print("The Result (a**b) : ", pow)
    return pow

print(" \t ** CALCULATOR PROGRAM ** ")
print(" + for ADDITION ")
print(" - for SUBTRACTION ")
print(" * for MULTIPLICATION ")
print(" / for DIVISION")
print(" // for FLOOR DIVISION")
print(" % for MODULUS ")
print(" ** for EXPONENT ")

i=0
while (i<10):
    print()
    choice=input("Enter your choice here : ")
    
    if choice=="+":
        print("\t -> OPERATION CHOOSEN : ADDITION")
        x,y=takeInput()
        output=addition(x,y) 
    elif choice=="-":
        print("\t -> OPERATION CHOOSEN : SUBTRACTION")
        x,y=takeInput()
        output=subtraction(x,y)
    elif choice=="*":
        print("\t -> OPERATION CHOOSEN : MULTIPLICATION")
        x,y=takeInput()
        output=multiply(x,y)
    elif choice=="/":
        print("\t -> OPERATION CHOOSEN : DIVISION")
        x,y=takeInput()
        output=division(x,y)
    elif choice=="//":
        print("\t -> OPERATION CHOOSEN : FLOOR DIVISION")
        x,y=takeInput()
        output=floorDivision(x,y)
    elif choice=="%":
        print("\t -> OPERATION CHOOSEN : MODULUS")
        x,y=takeInput()
        output=modulus(x,y)
    elif choice=="**":
        print("\t -> OPERATION CHOOSEN : EXPONENT ")
        x,y=takeInput()
        output=power(x,y)
    else:
        print("-> Invalid Operation choosen. Please try again!")
    i+=1
