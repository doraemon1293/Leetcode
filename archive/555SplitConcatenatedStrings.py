# coding=utf-8
'''
Created on 2017å¹?6æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [max(s, s[::-1]) for s in strs]
        ans = "".join(strs)
        for i in xrange(len(strs)):
            left = "".join(strs[:i])
            right = "".join(strs[i + 1:])
            for j in xrange(len(strs[i])):
                ans = max(ans, strs[i][j:] + right + left + strs[i][:j])
                ans = max(ans, strs[i][::-1][j:] + right + left + strs[i][::-1][:j])

        return ans


print Solution().splitLoopedString(["ab", "xy", "cd", "aaa", "bab"])
