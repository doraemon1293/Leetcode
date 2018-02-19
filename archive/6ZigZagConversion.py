# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = []
        if len(s) <= numRows or numRows == 1:
            return s
        for i in xrange(min(numRows, len(s))):
            index = i
            flag = True
            gap = 1
            while index < len(s):
                if gap != 0:
                    ans.append(s[index])
                if flag:
                    gap = 2 * (numRows - 1) - 2 * i
                    index += gap
                    flag = False
                else:
                    gap = 2 * i
                    index += gap
                    flag = True
        return "".join(ans)


print Solution().convert("12", 1)

