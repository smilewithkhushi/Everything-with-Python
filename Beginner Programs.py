#WAP TO CREATE PATTERNS USING LOOPS
for i in range(0,5):
    for j in range(0, i+1):
        print("*", end='')
    print()

print()
#WAP TO REVERSE THE NUMBER ENTERED BY THE USER
print("\n ** REVERSE OF USER INPUT : PROGRAM **")
numInput=input("Enter any value here : ")
val=[]
j=-1
for i in range(0, len(numInput)):
    val.append(numInput[j])
    j-=1
print("Reversed : ", val)
print()

#WAP TO CALCULATE SUM OF 10 NATURAL NUMBERS
sum=0
for i in range(0,11):
    sum+=i
print("Sum of 10 natural numbers (using for loop) : ", sum)

sum1=0
i=0
while i<11:
    sum1+=i
    i+=1
print("Sum of 10 natural numbers (using while loop) : ",sum1)
print()

#WAP TO CALCULATE SUM OF ODD AND EVEN NUMBERS

sumOdd=sumEven=0
odd=1
even=0
i=0
while (i<25):
    sumOdd+=odd
    sumEven+=even
    odd+=2
    even+=2
    i+=1

print(" -> USING WHILE LOOP")
print("Sum of Odd numbers btw 0 and 50 : ", sumOdd)
print("Sum of Even numbers btw 0 and 50 : ", sumEven)
print()

sumOdd1=sumEven1=0
for i in range(0,21,2):
    sumEven1+=i
for i in range(1,21,2):
    sumOdd1+=i
    
print(" -> USING FOR LOOP")
print("Sum of even numbers btw 0-20 : ", sumEven1)
print("Sum of odd numbers btw 0-20 : ", sumOdd1)


print()
