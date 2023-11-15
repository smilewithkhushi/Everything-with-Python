
#Define a class student to store has/her name and marks in three subjects. Use a class variable to store the
#maximum average marks of the class. Use constructor and destructor to initialize and destroy the objects

class Student: #class name
    maxavg=0
    result=[]
    
    def __init__(self):    #constructor
        count=int(input("-> How many student details do you want to enter? "))
        marksList={}
        
        for i in range(0, count):
            name=input("\n -> Enter the name of the student : ")
            marks=list(map(float, (input("-> Enter the marks in 3 subjects : ").split())))
            marksList[name]=marks
        
        
        #calculating the average marks from dictionary of students
        avgMarks={}
        for i in marksList:
            avg=0
            for j in marksList[i]:
                avg+=(j/3)
            avgMarks[i]=avg
        
            
        #finding the maximum average marks and store the name and scores individually
        maxAvg=0
        temp=0
        for i in avgMarks:
            if avgMarks[i]>maxAvg:
                temp=i
                maxAvg=avgMarks[i]
                
        result=[temp, maxAvg]
        
        self.result=result
        self.avgMarks=avgMarks
        self.marksList=marksList

    def showOutput(self):
        return self.result
    
    def displayData(self):
        print("\n \t ========================== \n \n  \t ** DATA COLLECTED FROM STUDENTS ** \n")
        print("NAME \t\t TOTAL MARKS \t\t AVERAGE MARKS")
        for name in self.marksList:
            print(name, "\t\t", self.marksList[name], "\t\t", self.avgMarks[name])
        
        print("\n \t ========================== \n")

while(True):
    print("\n \t __ QUESTION 15 : LIST PROGRAMS ___ \n")
    obj1=Student()
    obj1.displayData()
    result=obj1.showOutput()
    print("\n-->RESULT \n >> The maximum average marks of the class is ", result[1], "\n >> ", result[0], " has scored the highest marks in the class")
    ch=input("\n Do you want to continue(y/n) : ")
    if (ch=='n' or ch=='N' or ch=='no'):
        break
    #ahhaahhahaha
