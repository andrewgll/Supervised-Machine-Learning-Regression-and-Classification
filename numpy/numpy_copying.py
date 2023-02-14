import numpy as np

a = np.array([1,2,3])
b = a 
b[0] = 42
print(b) # changed in both
print(a) # here also

b = a.copy() # copying 
b[0] = 32
print(b) # they are different now
print(a) # and here also