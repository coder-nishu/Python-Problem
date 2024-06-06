#Create a 2-by-5 array containing reverse order of the even integers from 2 through 10 inthe first row and the odd integers from 1 through 9 in the second row.
import numpy as np

array = np.array([[x for x in range(10,1,-2)],[x for x in range(1,10,2)]])
print(array)
array.dtype