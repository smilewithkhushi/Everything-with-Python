#LIST PROGRAM - QUESTION 4


def createSet():
    num=input("\nEnter the number here : ")
    lst=[int(x) for x in str(num)]
    if (float(num)>=10):
        setDigit=set()
        for i in lst:
            setDigit.add(i)
        return setDigit
    else:
        print(" ERROR : INVALID NUMBER ! Try again ")
        creatSet()

print("QUES 4 : This program inputs a number and returns its digits in a set!")
result=createSet()
print()
print("-> The Set Formed : ", result)
