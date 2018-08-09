# Author:Patrick
import numpy as np  # 引入numpy模块
import pandas as pd

# pandas中的merge和concat类似,但主要是用于
# 两组有key column的数据,统一索引的数据.
# 通常也被用在Database的处理当中.
# 定义资料集并打印出
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left, '\n' * 2, right, '\n')
# 依据key column合并，并打印出
res = pd.merge(left, right, on='key')
print(res)
print('\n')

# 依据两组key合并
# 合并时有4种方法how = ['left', 'right', 'outer', 'inner']，预设值how='inner'。
# 定义资料集并打印出
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left, '\n' * 2, right, '\n')
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print('inner=', '\n', res, '\n' * 2)
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print('outer=', '\n', res, '\n' * 2)
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print('left=', '\n', res, '\n' * 2)
res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print('right=', '\n', res, '\n' * 2)

# indicator=True会将合并的记录放在新的一列

# 定义资料集并打印出
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print('df1=', '\n', df1, '\n' * 2, 'df2=', '\n', df2, '\n' * 2)

# 依据col1进行合并，并启用indicator=True，最后打印出
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
print('\n')

# 自定indicator column的名称，并打印出
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)
print('\n')

# 依据index合并
# 定义资料集并打印出
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print('left=', '\n', left, '\n' * 2, 'right=', '\n', right, '\n' * 2)
# 依据左右资料集的index进行合并，how='outer',并打印出
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
print('\n')

# 依据左右资料集的index进行合并，how='inner',并打印出
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
print('\n')

# 解决overlapping的问题
# 定义资料集
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print('boys=', '\n', boys, '\n' * 2, 'girls=', '\n', girls, '\n' * 2)
# 使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
