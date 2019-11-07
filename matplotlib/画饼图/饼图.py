# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
a = np.random.randn(985, 88)
filename = "data.xlsx"
df = pd.DataFrame(a)
print(filename)
df = pd.read_excel(filename, '01-航运公司')
#labels = '1', '2', '3', '4', '5' # 自定义标签
for i in range(5,7):
    a = np.array(df['1-{}'.format(i)].value_counts(normalize=True,sort=False))  # 每个标签占多大
    sizes = []
    for item in a:
        sizes.append(item)
    labels = '1','2','3','4','5'
    explode = (0, 0.1, 0, 0, 0)  # 将某部分爆炸出来
    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        pctdistance=1.1,
        labeldistance=1.3,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
    # autopct，圆里面的文本格式，%1.1f%%表示小数有1位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    plt.legend(labels, loc=2)
    plt.axis('equal')  # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.show()


# if __name__=="__main__":
#     main()