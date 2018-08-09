# Author:Patrick
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 使用plt.xlim设置x坐标轴范围：(-1, 2)；
# 使用plt.ylim设置y坐标轴范围：(-2, 3)；
# 使用plt.xlabel设置x坐标轴名称：’I am x’；
#  使用plt.ylabel设置y坐标轴名称：’I am y’；
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('i am x')
plt.ylabel('i am y ')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()
