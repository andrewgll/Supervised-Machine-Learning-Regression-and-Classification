import numpy as np

a = np.zeros((2,3)) # create array 2 by 3 filled with zeroes

print(a)

a = np.ones((2,3), dtype=np.int32)

print(a)

a = np.full((2,3), 5.0)
print(a)

a = np.eye(3) # generate array with 3 on diagonal
print(a)

a = np.arange(20)
print(a)

a = np.linspace(0,10,5) # create array with equal space from 0 to 10 with 5 elements   
print(a)