#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-5))


# 定义一个什么事也不做的空函数
def nop(x):
    pass


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#返回多值其实就是返回一个tuple
r = move(100, 100, 60, math.pi / 6)
print(r)
(151.96152422706632, 70.0)

