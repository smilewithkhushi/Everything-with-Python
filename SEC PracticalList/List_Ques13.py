"""
PRACTICAL LIST QUESTION 13

Write a function to multiply two non-negative numbers by repeated addition.
For example, 7*5 = 7+7+7+7+7. 

"""
print("Write a function to multiply two non-negative numbers by repeated addition. \n")

num1=int(input("Enter a number : "))
num2=int(input("Enter another number : "))
result=0
if (num1>0 and num2>0):
    for i in range(0,num1):
        result+=num2
        print(num2,end=" + ")
    print("0 = ", result)
else:
    print("Enter valid numbers!")
