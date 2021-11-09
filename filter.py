#!usr/bin/env python3
# _*_ coding: utf-8 _*_

#python 内置filter() 函数用于过滤序列
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A','', 'B',None, 'C', ' '])))

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

#打印1000以内素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
