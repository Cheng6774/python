#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick


# ord()函数获取字符的整数表示
# chr()函数把编码转换为对应的字符
print(ord('A'),
      ord('中'),
      chr(66),
      chr(25991))

# 对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'),
      '中文'.encode('utf-8'))

# 把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'),
      b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 传入errors='ignore'忽略错误的字节
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

# 计算str包含多少个字符
print(len('ABC'),
      len('中文'),
      len(b'ABC'),
      len(b'\xe4\xb8\xad\xe6\x96\x87'),
      len('中文'.encode('utf-8')))

# 格式化
print('Hello, %s' % 'world',
      'Hi, %s, you have $%d.' % ('Michael', 1000000))
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('%2d-%2d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)  # %%表示转义
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%s,你的成绩提升' % '小明', '%.1f%%' % r)
