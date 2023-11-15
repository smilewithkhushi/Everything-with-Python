#question 7 - LIST PROGRAM

def menu():
    print("\n \t\t\t PROGRAM 7")
    print("\t\t =========================")
    print("\t\t\t MENU : ")
    print("\t1- Find the length of the string")
    print("\t2- Find the maximum of three strings")
    print("\t3- Find the string and replace vowels with #")
    print("\t4- Find the number of words in a given string")
    print("\t5- Check if string is a palindrome or not")
    print("\t\t =========================")
   

def maxOfStrings(a,b,c):
    if (a.isdigit() and b.isdigit()and c.isdigit):
        max=a
        if (b>max):
            max=b
        if (c>max):
            max=c
        return max
    else:
        max=len(a)
        l2=len(b)
        l3=len(c)
        if (l2>max):
            max=b
        if (l3>max):
            max=c
        else:
            max=a
        return max
    
        if (max==l2==l3):
            if (a>b and a>c):
                max=a
            elif (b>a and b>c):
                max=b
            elif (c>a and c>b):
                max=c
            return max
        else:
            return max

def replaceVowels(a):
    new=""
    for i in a:
        if (i=='a' or i=='e' or i=='o' or i=='i' or i=='u'):
            new+="#"
        else:
            new+=i
    return new

def countWords(a):
    count=0
    for i in a:
        if (i==" " or i=="\t" or i=="\n" or i=="r"):
            count+=1
    return count

def pallindromeTest(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
            
        
ch="y"
menu()
while(ch=='y' or ch=="Y"):
    
    choice=int(input("\n -> Enter your choice from the menu : "))
    if (choice==1):
        print("\n\t OPERATION CHOOSEN : LENGTH OF THE STRING \n")
        str_input=input("Enter the string : ")
        lngth=len(str_input)
        print("--> Length of the string - " , lngth)
        
    elif (choice==2):
        print("\n\t OPERATION CHOOSEN : MAXIMUM OF THREE STRINGS \n")
        str1=input("Enter the first string : " )
        str2=input("Enter the second string : " )
        str3=input("Enter the third string : " )
        str_max=maxOfStrings(str1,str2,str3)
        print("--> The maximum of three strings is : ",str_max)
        
    elif (choice==3):
        print("\n\t OPERATION CHOOSEN : REPLACE VOWELS WITH # \n")
        str_input=input("Enter the string : ")
        str_vow=replaceVowels(str_input)
        print("-->The new string - " , str_vow)
        
    elif (choice==4):
        print("\n\t OPERATION CHOOSEN : COUNT NUMBER OF WORDS \n")
        str_input=input("Enter the string : ")
        wordCount=countWords(str_input)
        print("-->Total number of words in string - " , wordCount)
        
    elif (choice==5):
        print("\n\t OPERATION CHOOSEN : PALLINDROME TEST \n")
        str_input=input("Enter the string : ")
        result=pallindromeTest(str_input)
        if (result):
            print("--> The string " ,str_input, " is a pallindrome")
        else:
            print("--> The string " ,str_input, " is not a pallindrome")
            
    else:
        print("\n  ** ERROR : ENTER A VALID CHOICE ***\n")

    ch=input("\n -> Do you want to continue (y/n) : ")

print(" \t \t PROGRAM ENDS HERE ")
        
