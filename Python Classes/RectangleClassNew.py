class rectangle:
    def __init__(self, l , b):
        self.length=l
        self.breadth=b
        self.dict={}

    def setLength(self, num):
        self.length=num
        return self.length
        
    def setBreadth(self, num):
        self.breadth=num
        return self.breadth
        
    def getBreadth(self):
        print("- Breadth : ", self.breadth)

    def getLength(self):
        print("- Length : ", self.length)
        
    def area(self):
        self.area=(self.length*self.breadth)
        return self.area

    def perimeter(self):
        self.peri=2*(self.length+self.breadth)
        return self.peri
        
    def dictStore(self, count):
        name="Rectangle "+str(count+1)
        ar=self.area()
        pr=self.perimeter()
        data=[ar, pr]
        self.dict[name]=data
        
    def showDict(self):
        print()
        print(" - Dictionary Stored : { " , end="")
        for i in self.dict:
            print(i , " : " ,  self.dict[i], "," , end="")
        print("}")
            
def operationList():
    print("\n \t ***********************")
    print("\t 1. Update the length ")
    print("\t 2. Update the breadth ")
    print("\t 3. Retrieve the length ")
    print("\t 4. Retrieve the breadth ")
    print("\t 5. Print the area ")
    print("\t 6. Print the perimeter ")
    print("\t 7. Store rectangle coordinates in dictionary ")
    print("\t ***********************")
    print()
    
ch="y"
print()
print("\t ** PYTHON PROGRAM TO CREATE RECTANGLE CLASS AND PERFORM OPERATIONS ** \n")
operationList()
    
while (ch=="y" or ch=="Y"):
    l=float(input("Enter the length : "))
    b=float(input("Enter the breadth : "))
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
        area=rt.area()
        print("- Area : ", area)
        
    elif (choice==6):
        peri=rt.perimeter()
        print("- Perimeter : ", peri)
        
    elif (choice==7):
        count=int(input("How many rectangles do you have : "))
        for i in range(0, count+1):
            print("~~ For rectangle ", i+1)
            l=float(input("\tEnter the length : "))
            b=float(input("\tEnter the breadth : "))
            rt.setLength(l)
            rt.setBreadth(b)
            rt.dictStore(i)
            rt.showDict()      
    
    else:
        print("\t !! INVALID CHOICE : TRY AGAIN !! ")

    print()
    ch=input("Do you want to continue(y/n) : ")

print()
print("~~~ PROGRAM ENDS HERE ~~~")
