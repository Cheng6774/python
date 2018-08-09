# Author:Patrick
import numpy as np
A = np.arange(2,14).reshape((3,4))
# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])

print(np.argmin(A))  # 0
print(np.argmax(A))  # 11
print('\n')

print(np.mean(A))
print(np.average(A))
print(A.mean())
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A))
print(np.nonzero(A))# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))
print('\n')

A = np.arange(14,2, -1).reshape((3,4))
print('原矩阵=',A)
print(np.sort(A))
print('\n')

print('原矩阵=',A)
print(np.transpose(A))
print(A.T)
print('\n')

print('原矩阵=',A)
print(np.clip(A,5,9))
