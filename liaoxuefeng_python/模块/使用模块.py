#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args == 2):
        print('hello, %s!' % args[1])
    else:
        print('too many arguments!')


if__name__ = '__main__'
test()



# 模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


print(greeting('jack'))
