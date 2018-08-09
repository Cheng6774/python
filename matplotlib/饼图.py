# Author:Patrick
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  # 自定义标签
sizes = [15, 30, 45, 10]  # 每个标签占多大
explode = (0, 0.1, 0, 0)  # 将某部分爆炸出来

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# autopct，圆里面的文本格式，%1.1f%%表示小数有1位，整数有一位的浮点数
# shadow，饼是否有阴影
# startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
plt.axis('equal')  # 设置x，y轴刻度一致，这样饼图才能是圆的
plt.show()
