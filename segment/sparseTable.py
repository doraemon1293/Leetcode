# coding=utf-8
'''
Created on 2017å¹?10æœ?16æ—?

@author: Administrator
'''
import math


def rmq(nums):
    N = int(math.ceil(math.log(len(nums), 2)))
    maxNum = [[-float("inf")] * N for _ in xrange(len(nums))]
    minNum = [[float("inf")] * N for _ in xrange(len(nums))]
    for i in xrange(len(nums)):
        maxNum[i][0] = nums[i]
        minNum[i][0] = nums[i]
    for j in xrange(1, N):
        for i in xrange(len(nums)):
            if i + 2 ** (j - 1) < len(nums):
                maxNum[i][j] = max(maxNum[i][j - 1], maxNum[i + 2 ** (j - 1)][j - 1])
                minNum[i][j] = min(minNum[i][j - 1], minNum[i + 2 ** (j - 1)][j - 1])
    return maxNum, minNum


def query(maxNum, minNum, i, j, maxOrMin):
    k = int(math.floor(math.log(j - i + 1, 2)))
    if maxOrMin == "max":
        return max(maxNum[i][k], maxNum[j - 2 ** k + 1][k])
    elif maxOrMin == "min":
        return min(minNum[i][k], minNum[j - 2 ** k + 1][k])


if __name__ == "__main__":
    nums = [3, 2, 4, 5, 6, 8, 1, 2, 9, 7]
    maxNum, minNum = rmq(nums)
    i, j = 0, 6
    print query(maxNum, minNum, i, j, "max")

