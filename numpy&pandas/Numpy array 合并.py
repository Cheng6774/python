# Author:Patrick
import numpy as np  # 引入numpy模块
import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print(np.vstack((A, B)))  # vertical stack
C = np.vstack((A, B))
print(A.shape, C.shape)  # A是一个拥有3项元素的数组（数列），而合并后得到的C是一个2行3列的矩阵。
print('\n')

D = np.hstack((A, B))  # horizontal stack
print(D)
print(A.shape, D.shape)
print('\n')

print(A[np.newaxis, :])
print(A[np.newaxis, :].shape)
print(A[:, np.newaxis])
print(A[:, np.newaxis].shape)
print('\n')

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack
print('C=', C)
print('D=', D)
print('C结构', C.shape, 'D结构', D.shape)

# np.concatenate()
C = np.concatenate((A, B, B, A), axis=0)  # 将A,B转置后垂直合并
print(C)
print('\n')

D = np.concatenate((A, B, B, A), axis=1)  # 将A,B转置后水平合并
print(D)
