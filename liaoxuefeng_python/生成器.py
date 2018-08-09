#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

g=(x*x for x in range(10))
#逐个打印
print(next(g))
print(next(g))

g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break