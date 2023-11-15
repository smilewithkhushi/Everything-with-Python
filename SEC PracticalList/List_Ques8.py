#QUESTION 8 - LIST PROGRAM

def menu():
    print("\n \t\t\t PROGRAM 8")
    print("\t\t =========================")
    print("\t THIS PROGRAM PERFORMS FOLLOWING TASKS : ")
    print("\t1- Check if all elements in list are numbers or not")
    print("\t  -> If it is a numeric list, then count number of odd values in it ")
    print("\t  -> If list contains all strings, then display largest String in the list")
    print("\t2- Display list in reverse form")
    print("\t3- Find a specified element in list")
    print("\t4- Remove the specified element from the list")
    print("\t5- Sort the list in descending order")
    print("\t6- Accept 2 lists and find the common members in them")
    print("\t\t =========================")

def commonListMembers(lst1, lst2):
    min=len(lst1)
    l2=len(lst2)
    if (l2<min):
        min=l2
    
    commonList=[]
    for i in lst1:
        for j in lst2:
            if i==j:
                commonList.append(i)
    return commonList

def listType(lst):
    for i in lst:
        if (i.isdigit()==False):
            return False
    return True

def oddValCount(lst):
    count=0
    for i in lst:
        if (float(i)%2!=0):
            count+=1
    return count

def maxString(lst):
    maxLen=0
    for i in lst:
        if (len(i)>=maxLen):
            maxLen=len(i)
            result=i
    return result

def listReverse(a):
    a.reverse()
    return a

def listSort(a):
    a.sort()
    a.reverse()
    return a

def listSearch(num, lst):
    flag=0
    for i in range(len(lst)):
        if (lst[i]==num):
            flag+=1
            index=i
            
    if (flag>0):
        print("--> ", num, " found at " , index, " index in the list! " )
    else:
        print("--> ", num, " not found in the given list")

def listRemove(num,lst):
    flag=0
    for i in lst:
        if (i==num):
            lst.remove(i)
            index=i
            flag+=1
            
    if (flag>0):
        print("--> ", num, " removed from the list at index " , index, "\n THE NEW LIST : ", lst )
    else:
        print("--> ERROR REMOVING THE ELEMENT :: \t", num, " not found in the given list.")


ch="y"     
while(ch=='y' or ch=="Y"):
    menu()

    lst_input1=list(map(str, input("Enter the list elements here : ").split()))
    print("- The list entered : ", lst_input1)
    lst_input=[x for x in lst_input1]

    choice=int(input("\n -> Enter your choice from the menu : "))
    
    if (choice==1):
        print("\n\t OPERATION CHOOSEN : CHECK LIST ELEMENT TYPE \n")

        result=listType(lst_input)
        if (result==True):
            print("--> The List is numerical !")
            oddCount=oddValCount(lst_input)
            print("--> The total number of odd values in list are : ", oddCount)
        else:
            print("--> The List is not numerical !")
            max_string=maxString(lst_input)
            print("--> The maximum/largest string from the list is : ", max_string)        
        
    elif (choice==2):
        print("\n\t OPERATION CHOOSEN : LIST IN REVERSE FORM \n")
        
        lst_rev=listReverse(lst_input)
        print("--> The Reversed List is : ", lst_rev)
        
    elif (choice==3):
        print("\n\t OPERATION CHOOSEN : SEARCH SPECIFIED ELEMENT \n")
        num=input("Enter the element to be searched : ")
        listSearch(num, lst_input)
        
    elif (choice==4):
        print("\n\t OPERATION CHOOSEN : REMOVE SPECIFIED ELEMENT \n")
        num=input("Enter the element to be removed : ")
        listRemove(num, lst_input)
        
    elif (choice==5):
        print("\n\t OPERATION CHOOSEN : SORT LIST IN DESCENDING ORDER \n")
        rev=listSort(lst_input)
        print("--> The List in Descending order is : ", rev)   
            
    elif (choice==6):
        print("\n\t OPERATION CHOOSEN : COMMON MEMBERS FROM 2 LISTS \n")
        lst_input2=list(map(str, input("Enter the 2nd list elements here : ").split()))
        print("- The 2nd list entered : ", lst_input1)
        commonList=commonListMembers(lst_input1, lst_input2)
        print("\n--> The Common Members of the lists are ", commonList)   
            
    else:
        print("\n  ** ERROR : ENTER A VALID CHOICE ***\n")

    ch=input("\n -> Do you want to continue (y/n) : ")

print(" \t \t PROGRAM ENDS HERE ")
        
