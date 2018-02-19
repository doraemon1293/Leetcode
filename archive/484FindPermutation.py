# coding=utf-8
'''
Created on 2017å¹?5æœ?4æ—?

@author: Administrator
'''


class Solution(object):

    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s) + 1
        ans = range(1, n + 1)
        st = None
        for i, ch in enumerate(s + "I"):
            if ch == "D":
                if st == None:
                    st = i
                end = i + 1

            if ch == "I" and st != None:
                ans[st:end + 1] = reversed(ans[st:end + 1])
                st = None
        return ans


print Solution().findPermutation("IDDDI")
