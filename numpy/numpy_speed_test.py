from timeit import default_timer as timer
import numpy as np

a = np.random.rand(10000)
b = np.random.rand(10000)

A = list(a)
B = list(b)

T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot

def dot2():
    return np.dot(a,b)

start = timer()

for t in range(T):
    dot1()
end = timer()

t1 = end - start

start = timer()

for t in range(T):
    dot2()
end = timer()
t2 = end-start

print('Python3 list:', t1, 's')
print('numpy array:', t2, 's')
print('Faster by:',t1/t2, 'times')