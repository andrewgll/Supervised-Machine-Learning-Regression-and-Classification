import numpy as np

a = np.arange(1,7) # numbers from 1 to 6
print(a)

b = a.reshape((2,3)) # reshape array with 2 rows and 3 columns

print(b.shape)

b = a[np.newaxis, :] # add new axis to array
print(b)