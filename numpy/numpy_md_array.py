import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape)
print(a[0])
print(a[0][0])
print(a[0,0])
print(a[:,0])       # items in first column
print(a[0,:])       # items in first row
print(a.T)          # transpose array (merge into two columns)
print(np.linalg.inv(a))     # Compute the (multiplicative by inverse ^-1) inverse of a matrix

print(round(np.linalg.det(a)))     # Compute the determinant of matrix
print(np.diag(a))           # Compute diagonal of matrix