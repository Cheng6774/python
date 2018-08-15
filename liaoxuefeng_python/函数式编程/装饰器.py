#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Patrick

def now():
    return print('2015-3-25')
f=now
print(f())

print(now.__name__)
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')

now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()

import functools

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)

#改造成装饰器
def log(func):
    def wrapper():
        print('start execute')
        func()
        print('end execute')
    return wrapper
@log
def my_func():
    print('Hello World')
my_func()



