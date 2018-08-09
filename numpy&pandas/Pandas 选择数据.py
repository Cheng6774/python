# Author:Patrick
import numpy as np  # 引入numpy模块
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print('\n')

# 简单的筛选
print(df[0:3])  # 选择跨越多行或多列
print(df['20130102':'20130104'])
print('\n')

#根据标签 loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102',['A','B']])
print('\n')

#根据序列 iloc
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
print('\n')

#根据混合的这两种 ix
print(df.ix[:3,['A','B']])
print(df[df.A>8])
