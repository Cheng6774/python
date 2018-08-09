# Author:Patrick
import numpy as np  # 引入numpy模块
import pandas as pd

# axis (合并方向) axis=0是预设值
# 未设定任何参数时，函数默认axis=0
# 定义资料集
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
print(df1, '\n', df2, '\n', df3, '\n')

res = pd.concat([df1, df2, df3], axis=0)
print(res)  # 结果的index是0, 1, 2, 0, 1, 2, 0, 1, 2
print('\n')

# gnore_index (重置 index)
# 承上一个例子，并将index_ignore设定为True
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)  # index变0, 1, 2, 3, 4, 5, 6, 7, 8
print('\n')

# join (合并方式)
# join='outer'为预设值，因此未设定任何参数时，函数默认join='outer'。
# 此方式是依照column来做纵向合并，有相同的column上下合并在一起，
# 其他独自的column个自成列，原本没有值的位置皆以NaN填充。

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'],)
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'],)
print(df1, '\n', df2)
# 纵向"外"合并df1与df2
res = pd.concat([df1, df2], axis=0, join='outer')
print(res)
print('\n')

# #承上一个例子
# #纵向"内"合并df1与df2
res=pd.concat([df1,df2],axis=0,join='inner')
print(res)
print('\n')

#重置index并打印结果
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
print(res)