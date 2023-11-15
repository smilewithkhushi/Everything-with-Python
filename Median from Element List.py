#WAP that prints the median of two unsorted lists entered by the user.
list1=[1,3]
list2=[4,7]
newList=list1+list2
newList.sort()
print(newList)
l=len(newList)

if l%2==0: #even numbers
    mid=int(l/2)
    output=(newList[mid]+newList[mid+1])/2
else: #odd length
    mid=int(l/2)
    output=newList[mid]
print("The median of above list is : ", output)
