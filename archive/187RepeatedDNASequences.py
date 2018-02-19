# coding=utf-8
'''
Created on 2017å¹?8æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 10:
            return []
        ans = set()
        s10 = set()
        for i in xrange(n - 10 + 1):
            if s[i:i + 10] in s10:
                ans.add(s[i:i + 10])
            else:
                s10.add(s[i:i + 10])
        return list(ans)


s = "AAAAAAAAAAAA"
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print Solution().findRepeatedDnaSequences(s)

