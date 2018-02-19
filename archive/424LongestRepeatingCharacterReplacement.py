# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = Counter()
        st = 0
        ans = 0
        for en in xrange(len(s)):
            count.setdefault(s[en], 0)
            count[s[en]] += 1
            if en - st + 1 - count.most_common(1)[0][1] > k:
                count[s[st]] -= 1
                st += 1
            ans = max(ans, en - st + 1)
        return ans


s = "AABABBA"
k = 1
print Solution().characterReplacement(s, k)
