#30-08-2022

#program 1 : odd even number test
print("\n\t\t *** PRGRAM TO CHECK IF NUMBER IS EVEN OR ODD ***\n")
num=int(input("Enter a number : "))
if (num%2==0):
    print(num, " is an even number!")
else:
    print(num, " is an odd number!")

#program 2 : WAP to find greatest of three numbers
print("\n\t\t *** PRGRAM TO FIND GREATEST OF THREE NUMBERS ***\n")
a=float(input("Enter the 1st number : "))
b=float(input("Enter the 2nd number : "))
c=float(input("Enter the 3rd number : "))
max=a
if (b>max):
    max=b
elif (c>max):
    max=c
else:
    max=a
print(max, " is the greatest number out of three numbers")

#WAP to implement all types of operators
print("\n\t\t *** PRGRAM TO IMPLEMENT ALL TYPES OF OPERATORS ***\n")
print(" ---> Available operators : + , -, /, *, % ,//, ==, !=,>,<, >=, <= , and , or , not")
while (True):
    print()
    a=float(input("Enter operand 'a' : "))
    b=float(input("Enter operand 'b' : "))
    opr=input("Enter the operator : ")
    #arithmetic operators
    if (opr=='+'):
        print("->  Operation = a+b (Addition) \n->  Output = ",a+b)
    elif (opr=='-'):
        print("->  Operation = a-b (Subtraction) \n->  Output = ",a-b)
    elif (opr=='*'):
        print("->  Operation = a*b (Multiplication) \n->  Output = ",a*b)
    elif (opr=='/'):
        print("->  Operation = a/b (Division) \n->  Output = ",a/b)
    elif (opr=='%'):
        print("->  Operation = a%b (Modulus/Remainder) \n->  Output = ",a%b)
    elif (opr=='//'):
        print("->  Operation = a//b (Floor Division) \n->  Output = ",a//b)

    #comparision operators
    elif (opr=='=='):
        print("->  Operation = a==b (Equality Comparision) \n->  Output = ",a==b)
    elif (opr=='!='):
        print("->  Operation = a!=b (Inequality Comparision) \n->  Output = ",a!=b)
    elif (opr=='>'):
        print("->  Operation = a>b (Greater than) \n->  Output = ",a>b)
    elif (opr=='<'):
        print("->  Operation = a<b (Smaller than) \n->  Output = ",a<b)
    elif (opr=='>='):
        print("->  Operation = a>=b (Greater than or equal to) \n->  Output = ",a>=b)
    elif (opr=='<='):
        print("->  Operation = a<=b (Smaller than or equal to) \n->  Output = ",a<=b)
    
    #logical operators : and , or ,not    
    elif (opr=='and'):
        print("->  Operation = a and b (Logical AND) \n->  Output = ",a and b)
    elif (opr=='or'):
        print("->  Operation = a or b (Logical OR) \n->  Output = ",a or b)
    elif (opr=='not'):
        print("->  Operation = not a (Logical NOT) \n->  Output = ", not a )    
    else:
        print("ERROR : INVALID OPERATION ")
