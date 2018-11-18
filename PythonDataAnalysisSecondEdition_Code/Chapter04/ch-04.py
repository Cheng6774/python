'''
@Description: -*- coding: utf-8 -*-
@Author: Cheng
@Github: https://github.com/Cheng6774
@Date: 2018-11-18 17:40:27
@LastEditors: Cheng
@LastEditTime: 2018-11-18 19:38:57
'''

import numpy as np
from scipy.stats import scoreatpercentile
import pandas as pd

data = pd.read_csv("co2.csv", index_col=0, parse_dates=True)

co2 = np.array(data.co2)

print("The statistical valus for amounts of co2 in atmosphere : \n")
print("Max method : ", co2.max())
print("Max function : ", np.max(co2))

print("Min method : ", co2.min())
print("Min function : ", np.min(co2))

print("Mean method : ", co2.mean())
print("Mean function : ", np.mean(co2))

print("Std method : ", co2.std())
print("Std function : ", np.std(co2))

print("Median : ", np.median(co2))
print("Score at percentile 50 : ", scoreatpercentile(co2, 50))

###########################################线性代数
A = np.mat("2 4 6 ; 4 2 6 ; 10 -4 18")
print("A\n", A)

inverse = np.linalg.inv(A)
print("inverse of A \n", inverse)
print("Check \n", A * inverse)
print("Error \n", A * inverse - np.eye(3))

##############解线性方程组
A = np.mat("2 4 6;4 2 6;10 -4 18")
print("A\n", A)
b = np.array([0, 8, -9])
print("b\n", b)

x = np.linalg.solve(A, b)
print("Solution", x)
print("Check\n", np.dot(A, x))

###############计算特征值和特征向量
import numpy as np
A = np.mat("3 -2;1 0")
print("A\n", A)

print(("Eigenvalues", np.linalg.eig(A)))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("First tuple of eig", eigenvalues)
print("Second tuple of eig \n", eigenvectors)
for i in range(len(eigenvalues)):
    print("Left",np.dot(A,eigenvectors)[:,i])
    