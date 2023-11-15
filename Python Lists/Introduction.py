#Creating a list of fruits
fruits = ["apple", "banana", "cherry", "orange", "guava", 'grapes']
print(fruits)

#Priting the elements of the list
print("Printing fruits one by one:")
for x in fruits:
  print(x)

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = ["python", "programming", "coding", "computer"]
print(list1)
print(list2)
print(list3)

fruits = ["apples", "mango", "orange", "banana"]
print(fruits)

colors = ["pink", "red", "blue", "white"]
print(colors)

listnew = list1 + list2
print("New list from l1 and l2:", listnew)
#concatenation

#replication or repitition
listnew = list1 * 3
print("repitition of list 1 : ", listnew)

#traversing or printing the elements of the list one by one
print("\n -> Printing the elements of list1:")
for x in list1:
  print(x)

print("-> Printing the elements of list named colors: ")
for y in colors:
  print(y)

#printing table of 2
print("The table of 2 : ")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
  print("2 x", i, " = ", 2 * i)

#printing table of a number entered by the user
print()
num = int(input("Enter a number : "))
for i in range(0, 11):
  print(num, "x", i, " = ", num * i)
