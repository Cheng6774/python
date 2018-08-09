# Author:Patrick
import numpy as np  # 引入numpy模块
import pandas as pd

# 创建含 NaN 的矩阵
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
print('\n')

# 去掉有 NaN 的行或列, 可以使用 dropna
df.dropna(axis=0,  # 0: 对行进行操作; 1: 对列进行操作
          how='any')  # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
print(df.dropna())
print('\n')

# 将 NaN 的值用其他值代替, 比如代替成 0
print(df.fillna(value=0))
print('\n')

# 判断是否有缺失数据 NaN, 为 True 表示缺失数据:
print(df.isnull())
print('\n')

# 检测在数据中是否存在 NaN, 如果存在就返回 True
print(np.any(df.isnull()) == True)
