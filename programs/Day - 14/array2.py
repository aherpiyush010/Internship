import numpy as np

# Create a sample array of float64
arr = np.array([9.1, 8.2, 7.3, 6.4, 5.5], dtype=np.float64)
print(arr)

# Find the shape, size, and data type of the array
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)

# Change the data type of the array from float64 to int32
arr_int32 = arr.astype(np.int32)
print("Dtype after conversion :", arr_int32.dtype)
print("Array after conversion  :", arr_int32)

# Find the number of dimensions (ndim) of the array
print("Number of dimensions :", arr.ndim)