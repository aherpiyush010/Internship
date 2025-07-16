import numpy as np

# Create example 1D and 2D arrays
arr1 = np.array([10, 20, 30, 40, 50, 60, 70])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
# Extract first five elements in array 1
f1 = arr1[:5]
print(f1)  

# Extract last three elements in an array1
l = arr1[-3:]
print(l)  

# change every second element of array 1 
arr1[::2] = -1 
print(arr1)      

# extract an element from an 2d array (array2)
element = arr2[1, 2]  
print(element)          

# sllice a 2d array to get its first two rows and 2 columns 
e1 = arr2[:2 ,:2]
print(e1)

