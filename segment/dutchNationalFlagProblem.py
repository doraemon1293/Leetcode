# coding=utf-8
'''
Created on 2017å¹?8æœ?24æ—?

@author: Administrator
'''

from random import shuffle
arr = range(10) + [6, 6, 6, 6]
shuffle(arr)
i = j = 0
n = len(arr) - 1
mid = 6
print arr
while j <= n:
    if arr[j] < mid:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1
    elif arr[j] > mid:
        arr[j], arr[n] = arr[n], arr[j]
        n -= 1
    else:
        j += 1
    print arr
print arr

# arr will be 3 part (<mid,,mid,>mid)
