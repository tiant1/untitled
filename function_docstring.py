#!/bin/python
#coding: utf-8
def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。

    The two values must be integers.这两个数都应该为整数。'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

help(print_max)
print_max(3,5)
print(print_max.__doc__)