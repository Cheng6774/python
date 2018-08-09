#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

# 函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))

from functools import reduce


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


# map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 接受一个list并利用reduce()求积：
def prod(L):
    def f(x, y):
        return x * y

    return (reduce(f, L))


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
