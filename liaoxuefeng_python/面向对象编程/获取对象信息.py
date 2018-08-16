#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 20:20
# @Author  : Patrick Cheng
# @FileName: 获取对象信息.py
# @Software: PyCharm
# @Blog    : https://github.com/Cheng6774

# 使用type()判断基本类型
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))

# 如果一个变量指向函数或者类，也可以用type()判断
print('type(abs) =', type(abs))

# type()函数返回的是什么类型呢？它返回对应的Class类型
print(type(123) == type(456),
      type(123) == int,
      type('abc') == type('123'),
      type('abc') == str,
      type('abc') == type(123))

# 判断一个对象是否是函数
import types


def fn():
    pass


print(type(fn) == types.FunctionType,
      type(abs) == types.BuiltinFunctionType,
      type(lambda x: x) == types.LambdaType,
      type((x for x in range(10))) == types.GeneratorType)

# 判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
print(dir('ABC'))
print(len('ABC'), 'ABC'.__len__(), len('ABC') == 'ABC'.__len__())


# 自己写的类，如果也想用len(myObj)的话,自己写一个
class Mydog(object):
    def __len__(self):
        return 100


dog = Mydog()
print(len(dog))


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject
print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print('getattr(obj,\'z\')=',getattr(obj,'z',404))

# 也可以获得对象的方法
print('有属性power吗?',hasattr(obj,'power'))# 有属性'power'吗？
print('获取属性power',getattr(obj,'power'))
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn()) # 调用fn()与调用obj.power()是一样的