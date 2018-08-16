#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 17:25
# @Author  : Patrick Cheng
# @Filename: 访问限制.py
# @Software: PyCharm
# @Blog    : https://github.com/Cheng6774

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


# 无法从外部访问实例变量.__name和实例变量.__score
bart = Student('Bart Simpson', 59)


# 如果外部代码要获取name和score
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    # 访问实例变量.__name和实例变量.__score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 修改分数
    def set_score(self, score):
        if 0 <= score <= 100:#对参数做检查
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
print(bart.get_name())
bart.set_score(66)
print(bart.get_score())

#双下划线外部变量访问方法
print(bart._Student__score)

#以下方法是错误的，只是给bart新增了一个name变量
bart = Student('Bart Simpson', 59)
print(bart.get_name())
bart.__name = 'New Name' # 设置__name变量！
print(bart.__name)
#实际上class内部：
print('内部:',bart.get_name())

