# Author:Patrick
import numpy as np  # 引入numpy模块

A = np.arange(12).reshape((3, 4))
print(A)

print(np.split(A, 2, axis=1))
print(np.split(A, 3, axis=0))
print(np.array_split(A, 3, axis=1))
print(np.vsplit(A, 3))  # 等于 print(np.split(A, 3, axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.hsplit(A, 2))  # 等于 print(np.split(A, 2, axis=1))
