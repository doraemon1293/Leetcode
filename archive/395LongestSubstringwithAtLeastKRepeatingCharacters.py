# coding=utf-8
'''
Created on 2017å¹?7æœ?25æ—?

@author: Administrator
'''
from collections import Counter


class Solution(object):

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def foo(s, k):
            if s == "": return 0
            counter = Counter(s)
            for ch in counter:
                if counter[ch] < k:
                    return max([foo(x, k) for x in s.split(ch)])
            return len(s)

        return foo(s, k)


s = "weitong"
k = 2
print Solution().longestSubstring(s, k)

