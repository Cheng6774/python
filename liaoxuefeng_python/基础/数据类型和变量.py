# Author:Patrick

# 输入和输出
# name=input('please enter your name')
# print('hello',name)

# 转义字符\
print('I\'m learning\nPython.')
print('\\\t\\')
print(r'\\\t\\')  # r表示内部的字符串默认不转义

# 表示多行内容
print('''line1
line2
line3''')

# 布尔值可以用and、or和not运算。
print(True and True,

      True and False,

      False and False,

      5 > 3 and 3 > 1)

#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(9 / 3)
#一种除法是//，称为地板除，两个整数的除法仍然是整数
print(10 // 3)
#可以得到两个整数相除的余数
print( 10 % 3)

#变量赋值
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#作业打印出以下变量的值
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
print('n=',123)
print('f=',56.789)
print('s1=','\'hello, world\'')
print('s2=','\'hello, \\\'adam\\\'\'')
print('s3=','r\'hello, \"bart\"\'')
print('s4=','r\'\'\'hello,\nlisa!\'\'\'')

