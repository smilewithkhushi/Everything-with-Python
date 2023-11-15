#triplet with zero sum
flag=0
list=[-1, 0, 2, -3, 1]
for i in range(0, len(list)):
	for j in range(i+1, len(list)):
		for k in range(j+1, len(list)):
			if list[i]+list[j]+list[k]==0:
				print("triplet found! \n the triplet : ", list[i] , list[j], list[k])
				flag+=1
			else:
				pass

if flag!=0:
	print("program ends here")
else:
	print("triplet not found!")
