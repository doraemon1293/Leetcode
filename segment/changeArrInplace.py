# coding=utf-8
'''
Created on 2017�?10�?18�?

@author: Administrator
'''

arr = [1, 2, 3]


def foo(m):
    m = []


foo(arr)
print arr  # [1,2,3]


def foo(m):
    m[:] = []


foo(arr)
print arr  # [1,2,3]
