class rectangle:
    def __init__(self):
        self.length=0
        self.breadth=0

    def setLength(self, num):
        self.length=num
        return self.length
        
    def setBreadth(self, num):
        self.breadth=num
        return self.length
        
    def getBreadth(self):
        print("- Breadth : ", self.breadth)

    def getLength(self):
        print("- Length : ", self.length)
    def area(self):
        self.area=self.length*self.breadth
        print("- Area : ", self.area)

    def perimeter(self):
        self.peri=2*(self.length+self.breadth)
        print("- Perimeter : ", self.peri)

def operationList():
    print("\n \t ***********************")
    print("\t 1. Update the length ")
    print("\t 2. Update the breadth ")
    print("\t 3. Retrieve the length ")
    print("\t 4. Retrieve the breadth ")
    print("\t 5. Print the area ")
    print("\t 6. Print the perimeter ")
    print("\t ***********************")
    print()
    
ch="y"
print()
print("\t ** PYTHON PROGRAM TO CREATE RECTANGLE CLASS AND PERFORM OPERATIONS ** \n")
l=float(input("Enter the length : "))
b=float(input("Enter the breadth : "))
operationList()
    
while (ch=="y" or ch=="Y"):
    rt=rectangle(l,b)

    choice=int(input("\nEnter your choice : "))
    if (choice==1):
        num=float(input("-> Enter the updated length : "))
        rt.setLength(num)
    elif (choice ==2):
        num=float(input("-> Enter the updated breadth : "))
        rt.setBreadth(num)
    elif (choice==3):
        rt.getLength()
    elif (choice==4):
        rt.getBreadth()
    elif (choice==5):
        rt.area()
    elif (choice==6):
        rt.perimeter()
    else:
        print("\t !! INVALID CHOICE : TRY AGAIN !! ")

    print()
    ch=input("Do you want to continue(y/n) : ")

print()
print("~~~ PROGRAM ENDS HERE ~~~")
