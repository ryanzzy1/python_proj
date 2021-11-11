#!usr/bin/env python3
# _*_ coding: utf-8 _*_
# 指定按绝对值大小排序
sorted([45, 34, 43, -12, -32], key=abs)
#print(L)

list = [36, 5, -12, 9, -21]

keys = [36, 5, 12, 9, 21]
print(sorted(keys))
print(sorted(list))

# 反向排序 reverse=True
S = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(S)
