'''
#LINKEDIN LEARNING - ADVANCED PYTHON

Ques : WAP to return the prime factors of a number
INPUT : Integer value
OUTPUT : list of prime factors
'''

def isPrime(num):
    for i in range(1,num+1):
        if (num%i==0) and i!=1 and i!=num:
            return False    
    return True

def getFactors(num):
    factors=[]
    for i in range(2, num+1):
        if (num%i==0) and isPrime(i)==True:
            factors.append(i)
    return factors
            


num=int(input("-> Enter a number : "))
result=getFactors(num)
print(result)