# Author:Patrick
import numpy as np  # 引入numpy模块
import pandas as pd

#读取csv
data = pd.read_csv(r'C:\Users\cheng\Desktop\student.csv')

#打印出data
print(data)

#将资料存取成pickle
data.to_pickle('student.pickle')

