#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#利用递归函数计算阶乘
# N! = 1 *　２　＊　３　＊　．．．　＊　Ｎ
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print('fact(1) = ', fact(1) )
print('fact(5) = ', fact(5) )
print('fact(10) = ', fact(10) )
print('*******************\n')

# 尾递归
def fact_r(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)

print('fact_r(5) = ', fact_r(5))
print('fact_r(10) = ', fact_r(10))

# 利用递归移动汉诺塔

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')


