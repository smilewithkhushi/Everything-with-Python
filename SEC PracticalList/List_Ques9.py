#QUESTION 11 - STORE A MARKS OF STUDENTS IN 4 SUBJECTS

def menu():
    print("\n \t\t PROGRAM 9")
    print("\t\t =========================")
    print("\t\t\t THIS PROGRAM PERFORMS FOLLOWING TASKS : ")
    print("\t Stores the list of student names ")
    print("\t 1- Performs Linear/Binary Search for an element ")
    print("\t 2- Sort the elements using bubble sort/insertion sort/selection sort ")
    print("\t\t =========================")


ch="y"     
while(ch=='y' or ch=="Y"):
    menu()

    lst_input1=list(map(str, input("Enter the student names here : ").split()))
    print("-> The list of Students entered : ", lst_input1)
    lst_input=[x for x in lst_input1]

    choice=int(input("\n -> Enter your choice from the menu : "))
    
    if (choice==1):
        print("\n\t OPERATION CHOOSEN : SEARCH  \n")
        search_type=input("\t SEARCH OPTOINS AVAILABLE: \n 1-> Linear Search \n 2-> Binary Search \n Which search do you want to perform? : ")
        
        if (search_type==1):
            print("\t ** LINEAR SEARCH CHOOSEN ** ")
            ele=input("- Enter the element to be searched : ")
            res=linearSearch(ele,lst_input1)
            if (res==0):
                print("Element not found in the list! ")
            else:
                print("Element found in the list at ", res, "index")
            #oddCount=oddValCount(lst_input)
            #print("--> The total number of odd values in list are ", oddCount)
        elif (search_type==2):
            print("\t ** BINARY SEARCH CHOOSEN ** ")
            ele=input("- Enter the element to be searched : ")
            res=binarySearch(ele,lst_input1)
            if (res==0):
                print("Element not found in the list! ")
            else:
                print("Element found in the list at ", res, "index")
            
        else:
            print("\t !! ERROR : INVALID CHOICE !!")
            
    elif (choice==2):
        print("\n\t OPERATION CHOOSEN : SORT THE LIST ELEMENTS \n")
        if type(lst_input)=="int" || type(lst_input)=="float":
            lst_input.sort()
        lst_rev=listSort(lst_input)
        print("--> The Reversed List is : ", lst_rev)
        
    else:
        print("\n  ** ERROR : ENTER A VALID CHOICE ***\n")

    ch=input("\n -> Do you want to continue (y/n) : ")

print(" \t \t PROGRAM ENDS HERE ")
        
