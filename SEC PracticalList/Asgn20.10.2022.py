#20-10-2022 Assignment (Practical list question 11)
#assignment :bubble, insertion, selection sort
#linear and binary search

def insertionSort(arr):

      for i in range(1, len(arr)):
        key = arr[i]
 
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
      return arr
     

def bubbleSort(arr):
     size=len(arr)
     for i in range(0,size-1):
          for j in range(0,size-1):
               if arr[j]>arr[j+1]:
                    arr[j], arr[j+1]=arr[j+1],arr[j]
     return arr       


def selectionSort(arr):
     size=len(arr)
     for i in range(size-1):
          min=i
          for j in range(min+1, size):
               if arr[j]<arr[min]:
                    min=j

          if i!=min:
               arr[i], arr[min]=arr[min], arr[i]
     return arr
          
     
print("\n ** PROGRAM TO PERFORM SORTING ON A LIST OF ELEMENTS **\n\n ")

ch='y'
while(ch=='yes' or ch=='Y' or ch=='y'):
     lst=list(map(int, input("Enter all the elements for the list here : ").split()))
     print("\n-> The elements entered are ", lst)

     choice=int(input("\nChoices Available - \n 1. Bubble Sort \n 2. Insertion Sort \n 3. Selection Sort \n Enter the choice here : "))
     print()
     if choice==1:
          result=bubbleSort(lst)
          print("Resultant list after BUBBLE SORT : ", result)
     elif choice==2:
          result=insertionSort(lst)
          print("Resultant list after INSERTION SORT : ", result)
     elif choice==3:
          result=selectionSort(lst)
          print("Resultant list after SELECTION SORT : ", result)
     else:
          print("** INVALID CHOICE** ")
     print()
     ch=input("-- Do you wanna continue?? (y/n) : ")
     print()

print()
def linearSearch(lst, ele):
     for i in range(len(lst)):
          if lst[i]==ele:
               return i
     return 0

def binarySearch(lst,start, end,x):
     if (end>=start):
          mid=(start+end)//2
          if lst[mid] == x:
               return mid
          elif lst[mid] > x:
               return binarySearch(lst, start, mid - 1, x)
          else:
               return binarySearch(lst, mid + 1, end, x)
     else:
          return -1
     

print("\n ** PROGRAM TO PERFORM BINARY AND LINEAR SEARCH ON A LIST OF ELEMENTS **\n\n ")

ch='y'
while ch=='y' or ch=='Y' or ch=='Yes':
     lst=list(map(int, input("Enter all the elements for the list here : ").split()))
     print("\n-> The elements entered are ", lst)
     ele=int(input("\n Enter the element to be searched : "))

     choice=int(input("\nChoices Available - \n 1. Linear Search \n 2. Binary Search \n Enter the choice here : "))
     print()
     if choice==1:
          result=linearSearch(lst, ele)
          if result>0:
               print("Element found at ",result, " index in list.")
          else:
               print("Element not found! ")
     elif choice==2:
          result=binarySearch(lst, 0, len(lst)-1, ele)
          if result>0:
               print("Element found at ",result, " index in list.")
          else:
               print("Element not found! ")
     else:
          print("Invalid choice! ")
print("** PROGRAM ENDS HERE **")
