#Ques 1 : WAP to find the factorial of a number

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=i*fact
    return fact

print("\n\t\t *** CALCULATE FACTORIAL OF A NUMBER *** ")
n=int(input("Enter the number : "))
result=factorial(n)
print("-> The factorial of ", n, " is ",result)


def pallindrome(num):
    for i in range(0, len(num)):
        if (num[i]!=num[(len(num)-1)-i]):
            return 0
    return 1

print("\n\t\t *** CALCULATE IF NUMBER IS PALLINDROME OR NOT *** ")
n=input("Enter the number : ")
result=pallindrome(n)
if result==1:
    print("-> The number ", n, " is pallindrome")
else:
    print("-> The number ", n, " is not pallindrome")

def reverse(num):
    new=[]
    l=len(num)-1
    for i in range(0, len(num)):
        ele=num[l-i]
        new.append(ele)
        
    res=''.join([str(elem) for elem in new])
    return res

print("\n\t\t *** REVERSE THE NUMBER *** ")
n=input("Enter the number : ")
result=reverse(n)
print("-> The reverse of ", n, " is ",result)
