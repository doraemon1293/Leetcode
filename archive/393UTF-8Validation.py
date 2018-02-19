# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = 0
        data = [x % 256 for x in data]
        while n < len(data):
            if data[n] >> 3 == 0b11110:
                step = 3
            elif data[n] >> 4 == 0b1110:
                step = 2
            elif data[n] >> 5 == 0b110:
                step = 1
            elif data[n] >> 7 == 0b0:
                step = 0
            else:
                return False
            for i in xrange(n + 1, n + 1 + step):
                if i >= len(data):
                    return False
                if data[i] >> 6 != 0b10:
                    return False
            n = n + 1 + step
        return True


data = [197, 130, 1]
data = [235, 140, 4]
print Solution().validUtf8(data)
