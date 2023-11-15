#list question - program 3

#write a pythoon function to find the nth term of fibonacci sequence and
#its factorial . return the result as a list

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def calc(n):
    a=0
    b=1
    series=[a,b]
    for i in range(0,n-2):
        temp=a
        a=b
        b=temp+a
        series.append(b)

    num=series[n-1]
    fact=factorial(num)
    result=[series, num, fact]
    return result

n=int(input("Enter the value of n (no. of terms) : "))
result=calc(n)
print()
print("-> The Fibonacci Series with ",n," terms : ", result[0] )
print("-> The nth term of Fibonacci Series is : ", result[1])
print("-> The factorial of nth term from above series is : ", result[2])
