# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        m = re.match(" *([-+])?(\d+).*", str)
        # print m.groups()
        if m:
            num = int(m.group(2))
            if m.group(1) == "-":
                num = -num
            if -2 ** 31 > num:
                return -2 ** 31
            elif num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return num
        else:
            return 0


print Solution().myAtoi(" b11228552307")

