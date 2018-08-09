# Author:Patrick
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# set line styles
# l1, l2,要以逗号结尾, 因为plt.plot() 返回的是一个列表
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1, linestyle='--', label='squar line')
# plt.legend(loc='upper right')#表示图例将添加在图中的右上角


plt.legend(loc='upper right')
# 调整位置和名称
plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best')
plt.show()
#  'best' : 0,
#  'upper right'  : 1,
#  'upper left'   : 2,
#  'lower left'   : 3,
#  'lower right'  : 4,
#  'right'        : 5,
#  'center left'  : 6,
#  'center right' : 7,
#  'lower center' : 8,
#  'upper center' : 9,
#  'center'       : 10,
