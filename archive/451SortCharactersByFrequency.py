# coding=utf-8
'''
Created on 2017å¹?1æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(s)
        arr = sorted(counter.items(), key = lambda x: x[1], reverse = True)
        ans = []
        for x in arr:
            ans += x[0] * x[1]
        return "".join(ans)


s = "tree"
print Solution().frequencySort(s)
