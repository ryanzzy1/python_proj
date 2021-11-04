#!usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections.abc import Iterable
if (isinstance([], Iterable)):
    print('True')
if isinstance({}, Iterable):
    print('True')

if isinstance('abc', Iterable):
    print('True')

if isinstance((x for x in range(10)), Iterable):
    print('True')

l = [x for x in range(10)]
print(l)

if isinstance(100, Iterable):
    print('True')
else:
    print('False')

from collections.abc import Iterator
if isinstance((x for x in range(10)), Iterator):
    print('True')
else:
    print('False')

if isinstance([], Iterator):
    print('True')
else:
    print('False')

if isinstance('abc', Iterator):
    print('True')
else:
    print('False')

for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
