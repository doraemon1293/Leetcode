# coding=utf-8
'''
Created on 2016�?12�?14�?

@author: Administrator
'''


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        st = 0
        ans = 0
        for i in xrange(len(s)):
            if s[i] in char_index and st <= char_index[s[i]]:
                st = char_index[s[i]] + 1
            char_index[s[i]] = i
            ans = max(ans, i - st + 1)
        return ans


        # char_index储存距i�?近上�?次char出现的位�?
s = "abba"
print Solution().lengthOfLongestSubstring(s)

