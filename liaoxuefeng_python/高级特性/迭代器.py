#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

# isinstance()判断一个对象是否是Iterable可迭代对象
from collections import Iterable

print(isinstance([], Iterable),
      isinstance((), Iterable),
      isinstance({}, Iterable),
      isinstance((x for x in range(10)), Iterable),
      isinstance(100, Iterable))

# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#
# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator

print(isinstance([], Iterator),
      isinstance((), Iterator),
      isinstance({}, Iterator),
      isinstance((x for x in range(10)), Iterator),
      isinstance(100, Iterator))

# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3


print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1,2,3,4,5]:
    print(x)
print(isinstance([1, 2, 3, 4, 5],Iterator))
print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)
print(isinstance(iter([1, 2, 3, 4, 5]),Iterator))

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
