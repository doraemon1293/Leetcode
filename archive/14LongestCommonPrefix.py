# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        for i in range(len(strs[0])):
            for temp_str in strs:
                if i >= len(temp_str) or temp_str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


strs = ["aaaaa", "aab"]
print repr(Solution().longestCommonPrefix(strs))

