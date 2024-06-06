import numpy as np

# Create two arrays
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Multiply the two arrays element-wise
result = np.multiply(array1, array2)

# Print the resulting array
print("Resulting array after multiplication:")
print(result)

# Find the shape of the resulting array
shape_of_result = result.shape
print("Shape of the resulting array:", shape_of_result)

# Reshape the resulting array to a different form, e.g., (3, 2)
reshaped_result = result.reshape(3, 2)

# Print the reshaped array
print("Reshaped array:")
print(reshaped_result)
