import numpy as np
arr1= np.array([[1,2,3,4] , [5,6,7,8]])
arr2= np.array([[8,7,6,5],[9,5,4,2]])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

arr= np.concatenate((arr1,arr2),axis =0)
