# Author:Patrick
import numpy as np  # 引入numpy模块

# = 的赋值方式会带有关联性
a = np.arange(4)  # array([0, 1, 2, 3])
b = a
c = a
d = b
print(a)  # array([11,  1,  2,  3])
print('\n')

a[0] = 11
print(a)
b is a  # True
c is a  # True
d is a  # True
print('\n')

d[1:3] = [22, 33]  # array([11, 22, 33,  3])
print(a)  # array([11, 22, 33,  3])
print(b)  # array([11, 22, 33,  3])
print(c)  # array([11, 22, 33,  3])
print('\n')

# copy() 的赋值方式没有关联性
b = a.copy()  # deep copy
print(b)  # array([11, 22, 33,  3])
a[3] = 44
print(a)  # array([11, 22, 33, 44])
print(b)  # array([11, 22, 33,  3])
