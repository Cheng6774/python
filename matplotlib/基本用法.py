# Author:Patrick
import numpy as np
import matplotlib.pyplot as plt

# 定义x：范围是(-1,1);个数是50. 仿真一维数据组(x ,y)表示曲线1
x=np.linspace(-1,1,50)
y=2*x+1

# plt.plot画(x ,y)曲线. 使用plt.show显示图像.
plt.figure()
plt.plot(x,y)
plt.show()

