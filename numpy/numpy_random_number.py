import numpy as np

a = np.random.random((3,2)) # 0-1
print(a)

a = np.random.rand(3,2) # normal/Gaussinan

print(a)
print(a.mean(), a.var())

a = np.random.randint(1,10, size=(3,3))
print(a)

a = np.random.choice(5, size=10)
print(a)
a = np.random.choice([1,2,3], size=10)
print(a)