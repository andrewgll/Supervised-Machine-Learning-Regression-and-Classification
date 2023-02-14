import numpy as np

a = np.array([[1,23,4,5,6,7,8],[1,23,4,5,6,7,8]])
print(a.sum(axis=1))
print(a.mean(axis=None))
print(a.var(axis=None))
print(np.std(a,axis=None))
