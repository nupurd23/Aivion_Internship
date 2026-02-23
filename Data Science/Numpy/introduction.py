import numpy as np
lst = [1,2,3]
print(type(lst))

arr = np.array(lst)
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
zeros = np.zeros((3,5))
print(zeros)