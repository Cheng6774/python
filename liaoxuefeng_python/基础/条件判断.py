#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

# if
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

if age >= 18:
    print('adult')
elif age <= 6:
    print('kid')
else:
    print('teenager')

# 忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

if 1:
    print('true')

# input()返回的数据类型是str
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

a = float(input('身高（m）'))
b = float(input('体重（kg）'))
c = float('%2.1f' % (b / (a ** 2)))
print(c)
if c < 18.5:
    print('过轻')
elif c < 25:
    print('正常')
elif c > 28:
    print('过重')
elif c < 32:
    print('肥胖')
else:
    print('严重肥胖')
