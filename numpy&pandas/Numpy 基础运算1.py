# Author:Patrick
import numpy as np  # 为了方便使用numpy 采用np简写

a = np.array([10, 20, 30, 40])  # array([10, 20, 30, 40])
b = np.arange(4)  # array([0, 1, 2, 3])
print(a)
print(b)
print('\n')

c = a - b  # array([10, 19, 28, 37])
d = a + b  # array([10, 21, 32, 43])
e = a * b  # array([  0,  20,  60, 120])
f = b ** 2  # array([0, 1, 4, 9])
g = 10 * np.sin(a)  # array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])
print(b < 3)  # array([ True,  True,  True, False], dtype=bool)

a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2, 2))
print(a)
print(b)
print('\n')

c_dot = np.dot(a, b)
c_dot_2 = a.dot(b)
# array([[2, 4],
#       [2, 3]])
print(c_dot)
print(c_dot_2)
print('\n')


a = np.arange(8).reshape(2, 4)
print(a)

print(np.sum(a))
print(np.min(a))
print(np.max(a))
print('\n')

print('a=', a)
print('sum=', np.sum(a, axis=1))
print('max=', np.max(a, axis=1))
print('min=', np.min(a, axis=1))
