# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''
from collections import Counter


class Solution(object):

    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter()
        st = 0
        ans = 0
        for en in xrange(len(s)):
            count.setdefault(s[en], 0)
            count[s[en]] += 1
            while len(count) > 2:
                count[s[st]] -= 1
                if count[s[st]] == 0:
                    del count[s[st]]
                st += 1
            ans = max(ans, en - st + 1)
        return ans


s = "eceba"
print Solution().lengthOfLongestSubstringTwoDistinct(s)
