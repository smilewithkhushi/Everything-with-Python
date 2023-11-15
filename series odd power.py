#term=int(input("enter value of n="))
term=5
sum=1
j=1
print("1^0", end="")
for i in range(2,6):
	sum+=i**j
	print("+", i,"^",j, end="")
	j+=2
print("\n The sum of above series is ", sum)
		