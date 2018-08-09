#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

# 删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


# 要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

# 寻找素数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    main()


def is_palindrome(n):
    temp = str(n)
    if temp == temp[::-1]:  #::-1表示将列表或字符倒过来
        return n


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
