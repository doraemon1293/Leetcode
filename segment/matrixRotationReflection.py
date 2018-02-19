# coding=utf-8
'''
Created on 2017å¹?10æœ?18æ—?

@author: Administrator
'''

m = [[1, 2, 3], [4, 5, 6]]


def rotate90Degree(m):
    return map(list, zip(*m[::-1]))


def rotate180Degree(m):
    return map(lambda x:x[::-1], m[::-1])


def rotate270Degree(m):
    return map(list, zip(*m)[::-1])


def reflectionLeftRIght(m):
    return map(lambda x:x[::-1], m)


def reflectionUpDown(m):
    return m[::-1]


print rotate90Degree(m)
print rotate180Degree(m)
print rotate270Degree(m)
print reflectionLeftRIght(m)
print reflectionUpDown(m)
