# Author:Patrick
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)# 在二维平面中将每一个x和每一个y分别对应起来，编织成栅格

#plt.contourf把颜色加进去
# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap=plt.cm.hot)

#plt.contour函数划线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

#inline控制是否将Label画在线里面
plt.clabel(C,inline=True,fontsize=10)
plt.xticks()
plt.show()

