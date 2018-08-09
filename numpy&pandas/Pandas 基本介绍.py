# Author:Patrick
import numpy as np  # 引入numpy模块

import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
print('\n')

# DataFrame 的一些简单运用
dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print('\n')

print(df['b'])
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))  # 一组没有给定行标签和列标签的数据
print(df1)
print('\n')

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print('\n')

print(df2.dtypes)  # 查看数据中的类型
print(df2.index)  # 查看对列的序号
print(df2.columns)  # 每种数据的名称
print(df2.values)  # 所有df2的值
print(df2.describe())  # 数据的总结
print(df2.T)  # 翻转数据
print(df2.sort_index(axis=1, ascending=False))  # 对数据的 index 进行排序并输出
print(df2.sort_values(by='B'))  # 对数据 值 排序输出
