#list question 10

'''
WAP that prints armstrong numbers in the range 1 to 1000.
an armstrong number is number whose sum of cubes of the digits is equal to the number itself
'''
print("The armstrong numbers in  the range 1 to 1000 are : ")
for i in range(1,1000):
    num=str(i)
    sum1=0
    for j in num:
        sum1=sum1+int(j)**3
    if sum1==int(num):
        print(num, end=" , ")

    

        
