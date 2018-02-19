# coding=utf-8
'''
Created on 2017å¹?10æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        arr = []
        cur = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                arr.append(cur)
                cur = 1
            else:
                cur += 1
        arr.append(cur)
        for i in range(1, len(arr)):
            ans += min(arr[i], arr[i - 1])
        return ans


s = "10101"
print Solution().countBinarySubstrings(s)

