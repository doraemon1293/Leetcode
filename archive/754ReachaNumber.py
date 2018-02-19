# coding=utf-8
'''
Created on 5 Jan 2018

@author: Administrator
'''


class Solution:

    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        import math
        target = abs(target)
        n = int(math.sqrt(target * 2))

        while True:
            dif = n * (n + 1) // 2 - target
            if dif >= 0:
                if dif % 2 == 0:
                    return n
            n += 1

