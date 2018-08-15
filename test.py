#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
        return ax
    return ax

# 不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,3,5,7,9)
print(f())

#每次调用都会返回一个新的函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
