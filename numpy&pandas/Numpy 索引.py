# Author:Patrick
import numpy as np  # 引入numpy模块

A = np.arange(3, 15)
print(A[3])
print('\n')

A = np.arange(3, 15).reshape((3, 4))
print(A)
print(A[2])  # 打印某行
print(A[2][1])  # 打印某元素
print(A[2, 1])  # 打印某元素
print('\n')

print(A[1, 1:3])
print(A[2, :])  # 打印某行
print(A[:, 3])  # 打印某列
print('\n')

for row in A:  # 多行打印
    print(row)
print('\n')

for column in A.T:  # 多列打印
    print(column)
print('\n')

# 迭代输出,这一脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。而flat是一个迭代器，本身是一个object属性。
A = np.arange(3, 15).reshape((3, 4))
print(A.flatten())

for item in A.flat:
    print(item)
