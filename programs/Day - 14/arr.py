import numpy as np

 # 1D array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr1)

# Array of zeroes 
zeroes = np.zeros((10))
print(zeroes)

# array of ones 
arrof1 = np.ones((5))
print(arrof1)

# arre of even numbers from two to twenty 
arr2 = np.arange(2,21,2)
print(arr2)

# random array between 0 and 1 value 
arr3 = np.random.rand(10)
print(arr3)

# create an array of shape (3, 3) filled with the number 7
arr4 = np.full((3, 3), 7)
print(arr4)

# create an identity matrix of size 4x4
arr5 = np.eye(4)
print(arr5)
