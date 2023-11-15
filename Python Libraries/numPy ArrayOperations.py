from numpy.lib.function_base import add_newdoc_ufunc
import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
print(arr1, arr2)
print("\n->addition:",arr1+arr2)
print("\n->multiplication:",arr1*arr2)
print("\n->substraction:",arr1-arr2)
np.add(arr1, arr2)
arr3=np.array([7,8,9,10])
arr4=np.array([11,22,33,44])
np.add(arr3,arr4)
arr6=np.array([[4,5],[1,2,]])
#arr6=arr1+5
#print(arr1+5)

arr5=np.array([[4, 16, 25, 36, 49 ],[9,81, 121, 49, 36]])
sum1=np.sum(arr5)
sqrt1=np.sqrt(arr5)  #square root ehehehe
arr6=np.transpose(arr5)     #TRANSPOSE HEHE
matrix=np.array([[2,3,4,5,6],[2,4,5,6,7],[7,8,9,2,1],[5,7,8,9,2],[11,22,33,44,55]])
#
print("\n\n-> 😀2D array arr5 = ",arr5, "\nSum of elements of 2D array5 =", sum1, "\nSquare root of elements : ", sqrt1)
print("\n-> 😊Transpose of 2d array : \n", arr6)
print("\n-> 🤗Slicing of arr1 : ", arr1[2:5])
print("\n->😎 Slicing of arr5 : \n", arr5[2:, 2:])
print("\n->😈Slicing of BIG BOY MATRIX : \n", matrix[0: , 0:6:2 ])
