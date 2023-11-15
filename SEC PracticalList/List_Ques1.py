#list question 1

#function that takes lengths of three sides

def inputDimension():
    side1=float(input("Enter the side 1 : "))
    side2=float(input("Enter the side 2 : "))
    side3=float(input("Enter the side 3 : "))
    perimeter=side1+side2+side3
    s = (side1 + side2 +side3) / 2.
    area=(s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
    tup=(perimeter,area)
    return tup

p, a =inputDimension()
print()
print("-> Perimeter of given triangle : ", p)
print("-> Area of given triangle : ", a)
