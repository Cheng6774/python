#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

#list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)

#获得list元素的个数
print('len(classmates) =', len(classmates))

#索引来访问list中每一个位置的元素
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

#往list中追加元素到末尾
classmates.append('Jack')
print(classmates)

#元素插入到指定的位置，比如索引号为1
classmates.insert(1,'Peter')
print(classmates)

#删除list末尾的元素，用pop()方法
# 删除指定位置的元素，用pop(i)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

#某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1]='Sarah'
print(classmates)
