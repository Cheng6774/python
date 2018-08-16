#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 18:38
# @Author  : Patrick Cheng
# @Filename: 继承和多态.py
# @Software: PyCharm
# @Blog    : https://github.com/Cheng6774

# 定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），
# 而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
    def run(self):
        print('Animal is running...')
a=Animal()
a.run()
# 需要编写Dog和Cat类时，就可以直接从Animal类继承

class Cat(Animal):
    pass

class Dog(Animal):
    pass
# 子类获得了父类的全部功能
c=Cat()
c.run()
d=Dog()
d.run()

#子类的run()覆盖了父类的run()
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
c=Cat()
c.run()
d=Dog()
d.run()

# 定义一个class的时候，我们实际上就定义了一种数据类型
# 判断一个变量是否是某个类型可以用isinstance()
print('c is a animal?',isinstance(c,Cat))
print('d is a animal?',isinstance(d,Dog))
#也是Animal类型
print('c is Cat?',isinstance(c,Animal))
print('d is Dat?',isinstance(d,Animal))

# 如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类,反过来不行
b = Animal()
print(isinstance(b, Dog))