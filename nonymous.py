#!usr/bin/env python3
# _*_ coding: utf-8 _*_

l = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print(l)

# dectator
def now():
    print('2018-3-23')

f = now()


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

@debug
def hello():
    print("hello")

hello()

"""
带参数的装饰器

"""
def logging(level):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            print("[{0}]: enter {1}()".format(level, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return outwrapper

@logging(level="INFO")
def hello(a, b, c):
    print(a, b, c)

hello("hello", "good", "morning")

