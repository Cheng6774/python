'''
@Description: -*- coding: utf-8 -*-
@Author: Cheng
@Github: https://github.com/Cheng6774
@Date: 2018-11-18 17:40:27
@LastEditors: Cheng
@LastEditTime: 2018-11-18 19:07:50
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