# Final Mini Project
# Perform the following in one script:
# Create a 5x5 array of random integers between 1–100.
# Find the min, max, mean, and sum of the array.
# Replace all numbers > 50 with -1.
# Save the array to a .npy file.
# Load it back and print the contents.

import numpy as np

# Create a 5x5 array of random integers between 1–100
array = np.random.randint(1, 101, size=(5, 5))
print( array)

# Find the min, max, mean, and sum
min_val = np.min(array)
max_val = np.max(array)
mean_val = np.mean(array)
sum_val = np.sum(array)

print("Min:", min_val)
print("Max:", max_val)
print("Mean:", mean_val)
print("Sum:", sum_val)

# Replace all numbers > 50 with -1
array[array > 50] = -1
print("modified array :", array)



