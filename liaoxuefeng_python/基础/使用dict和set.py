#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 通过key放入
d['Adam'] = 90
print(d['Adam'])

#避免key不存在的错误
print('Tomas'in d)
print(d.get('Tomas'))
print(d.get('Tomas','没有'))

# 删除一个key
d.pop('Bob')

# 创建一个set，需要提供一个list作为输入集合
# 重复元素在set中自动被过滤：
s=set([1,2,3])
print(s)

# add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)

# remove(key)方法可以删除元素
s.remove(4)

# 两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1|s2)

a = ['c', 'b', 'a']
a.sort()
print(a)