import numpy as np
print(np.__version__)
print('Array numpy methods')
a = np.array([1,2,3])
print(a.shape)      # count elements in dimension
print(a.dtype)      # data type of array
print(a.ndim)       # number of dimension
print(a.size)       # total number of elements
print(a.itemsize)   # size in bytes of each element
print(a[0])         # first element


print('Array math operations')
a[0] = 10
print(a)
b = a * np.array([0,1,2])   # array multiplication
print(b)
l = [1,2,3]
j = np.array([1,2,3])
l.append(4)         # okay
#j.append(4)        # not okay
l += [4]            # okay
j += np.array([4])  # okay but added to each element
print(j)
print(l)

np_array = np.array([1,2,3])
p_array = [1,2,3]
np_array *= 3
print(np_array)
p_array *=3
print(p_array)

print(np.log(np_array))
print(np.sqrt(np_array))

# dot product

l1 = [1,2,3]
l2 = [3,4,5]

a1 = np.array(l1)
a2 = np.array(l2)

dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1,a2)

print(dot)

sum1 = a1 * a2
print(sum1)
dot = np.sum(sum1)
print(dot)

dot = a1 @ a2       # also calculates dot 
print(dot)
