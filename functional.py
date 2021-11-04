#!usr/bin/env python3
# _*_ coding: utf-8 _*_

x = abs(-13)
print(abs(-12))
print(x)

f = abs
print(f(-5))

def add(x, y, f):
    return f(x) + f(y)
x = -5
y = 9
f = abs
print('f(x) + f(y) = ',add(x,y,f))

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5])
print(list(r))

L= []
for n in [1, 2, 3, 4, 5, 6]:
    L.append(f(n))
print(L)

print(list(map(str, [1, 2, 3, 4, 5, 6])))

from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y

def char2nm(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2nm, '13567')))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2nm, s))

s = ['2', '4', '4', '6']
print(str2int(s))

def char2num(s):
    return GIGITS[s]

def str2int(s):
    return reduc(lambda x, y: x * 10 + y, map(char2num, s))

Cap = {'a': A, 'b': B, 'c': C, 'd': D, 'e': E, 'f': F, 'g': G,
       'h': H, 'i': I, 'j': J, 'k': K, 'l': L, 'm': M, 'n': N,
       'o': O, 'p': P, 'q': Q, 'r': R, 's': S, 't': T, 'u': U,
       'v': V, 'w': W, 'x': X, 'y': Y, 'z': Z}



