#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 17:18
# @Author  : Patrick Cheng
# @Filename: 类和实例.py
# @Software: PyCharm
# @Blog    : https://github.com/Cheng6774

# 定义类是通过class关键字
class Student(object):
    pass


bart = Student()
bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


# 第一个参数永远是self,把各种属性绑定到self

# 传入与__init__方法匹配的参数
bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)


# 数据封装
def print_score(std):
    print('%s:%s' % (std.name, std.score))


print_score(bart)


# 封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))


jack = Student('jack', 88)
jack.print_score()


# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
