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

#设置不同名字和位置
#gca='get current axis'的位置.plt.gca获取当前坐标轴信息. 使用.spines设置边框
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


#调整坐标轴使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：bottom.
# （所有位置：top，bottom，both，default，none）
ax.xaxis.set_ticks_position('bottom')

#使用.spines设置边框：x轴；使用.set_position设置边框位置:y=0的位置；
# （位置所有属性：outward，axes，data）
ax.spines['bottom'].set_position(('data', 0))

#使用.yaxis.set_ticks_position设置y坐标刻度数字或名称的位置：
# left.（所有位置：left，right，both，default，none）
ax.yaxis.set_ticks_position('left')
#使用.spines设置边框：y轴；使用.set_position设置边框位置：x=0的位置；
# （位置所有属性：outward，axes，data）
ax.spines['left'].set_position(('data',0))
plt.show()


