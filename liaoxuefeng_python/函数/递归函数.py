#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

#计算阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))

# 改成尾递归方式解决递归调用栈溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))

#汉诺塔的移动
# 表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# 三个点A B C ，先不考虑A点上有几个盘子，最终要实现移动至C点的逻辑大体步骤就三步，
# 以总共3个盘子为例，当3个盘子都在A点的时候，需要将2也就是(n-1)个盘子都移到B点上，这样才能将C点空出来，
# 存放最大的那个盘子，所以这一步逻辑表达出来就这样写move(n-1, a, c, b)，
# 这一步做完了就接着下一步，把A点的1个盘子移到C点，这里就是确定的数字1，
# 所以第二步的逻辑表达出来就如此写：move(1, a, b, c)，接下来就是逻辑上的第三步，
# 将B点上的2个(n-1)盘子移到C点，所以最后一步的逻辑表达出来就如此写：move(n-1, b, a, c)。
# 总体概括一下就是：除了只有一个盘子（一个盘子都不存在循环了）之外，不管总共是2个，3个，4个，5个.....
# 就把它想像划分成3个逻辑体，它就是按那3个步骤来循环，这样就简单了。
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3,'A','B','C')
