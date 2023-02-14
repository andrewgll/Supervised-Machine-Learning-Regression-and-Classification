import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b = a[0,:]      # only row 0
print(b)
b = a[0,1:3]    # only row 0 from 1st to 3rd element
print(b)
b = a[:,1]      # only column 1
print(b)
b = a[:,-1]     # only last column 
print(b)
b = a[-1,-1]    # last element
print(b)

a = np.array([[1,2],[3,4],[5,6]])
print(a)

bool_idx = a > 2
print(bool_idx)
print(a[bool_idx])
print(a[a > 2])     # print all elements which are greater than 2

b = np.where(a > 2, a, -1)  # where element > 2 set original value where not set -1
print(b)

a = np.array([10,2,3,4,19,22,87,123])

print(a)
b = [1,3,5] # fancy indexing 
print(a[b]) # b is indexes
even = np.argwhere(a%2==0).flatten()
print(a[even])