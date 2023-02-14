import numpy as np

a = np.array([[1,2],[3,4]])
print(a)

b = np.array([[5,6]])

c = np.concatenate((a,b)) # concats two array
c = np.concatenate((a,b.T), axis = 1) # concats two to one dimension
print(c)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.hstack((a,b)) # concat to array horisontaly
print(c)
c = np.vstack((a,b)) # concat to array verticaly
print(c)


