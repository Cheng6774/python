# Author:Patrick
import numpy as np
import matplotlib.pyplot as plt

# 均匀图中图
plt.figure()
plt.subplot(2, 2, 1)
# plt.subplot(2,2,1)表示将整个图像窗口分为2行2列, 当前位置为1,在第1个位置创建一个小图
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])

# plt.subplot(2,2,3)可以简写成plt.subplot(223),
plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])

plt.show()

# 不均匀图中图
# 整个图像窗口分为2行1列, 当前位置为1
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

# 第二行划分为三列，则将图划分成六个格，第一行三个格为一列，序号为1,2,3，
# 则第二行的第一个格为4
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

plt.subplot(235)
plt.plot([0, 1], [0, 3])

plt.subplot(236)
plt.plot([0, 1], [0, 4])

plt.show()  # 展示
