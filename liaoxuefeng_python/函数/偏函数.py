#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

print(int('12345', base=8))
print(int('12345', 16))


def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))

import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2('1000000', base=10)

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
print(int2('10010'))

kw = {'base': 2}
print(int('10010', **kw))

# 10作为*args的一部分自动加到左边
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))