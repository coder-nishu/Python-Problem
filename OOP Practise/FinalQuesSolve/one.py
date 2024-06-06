import numpy as np

# Constructing the matrix
matrix = np.array([
    [1, 10, 20, 30],
    [2, 15, 25, 35],
    [3, 20, 30, 40]          # Fourth row
])

print("Matrix:\n", matrix)
# Diagonal elements
diagonal = np.diagonal(matrix)
print("Diagonal Elements:", diagonal)

# Above diagonal elements
above_diagonal = np.diagonal(matrix, offset=1)
print("Above Diagonal Elements:", above_diagonal)

# Below diagonal elements
below_diagonal = np.diagonal(matrix, offset=-1)
print("Below Diagonal Elements:", below_diagonal)

column2to4 = matrix.T
print(column2to4)