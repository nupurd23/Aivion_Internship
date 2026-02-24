import numpy as np
arr= np.array([[7,3,2], [3,2,6],[9,8,4]])
arr = np.sort(arr, axis=1, kind= 'mergesort')

print(arr)