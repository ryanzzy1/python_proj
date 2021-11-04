#!usr/bin/env python3
# _*_ coding: utf-8 _*_

#iteration find max and min return tuple
from collections.abc import Iterable, Iterator

def findMinAndMax(L):
    if L == []:
        return (None,None)
    elif L != []:
        min = L[0]
        max = L[0]
        for i in L:
            if min > i:
                min = i
            if max < i:
                max = i
            i = i+1
        return(min, max)
"""
def findminmax(L):
    if len(L) > 0:
        return(min(L),max(L))
    else:
        return(None,None)
"""

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



