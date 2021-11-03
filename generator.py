#!usr/bin/env python3
# _*_ coding: utf-8 _*_

L = [x * x for x in range(10)]
print(L)
print('**********************')

g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)
print('**********************')

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(6)
print('**********************')

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)

print('//*******//')
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print('/****************/')

