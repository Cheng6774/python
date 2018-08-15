#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 匿名函数lambda x: x * x实际上就是
# def f(x):
    # return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

f=lambda x:x*x
print(f)
print(f(5))

# 作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

L = list(filter(lambda n:n%2==1, range(1, 20)))
print(L)