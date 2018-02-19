# coding=utf-8
'''
Created on 2017å¹?10æœ?18æ—?

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
