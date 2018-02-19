# coding=utf-8
'''
Created on 2017å¹?6æœ?29æ—?

@author: Administrator
'''


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s.startswith("0"): return 0
        fn = fn_1 = fn_2 = 1
        for i in xrange(1, len(s)):
            if s[i] != "0":
                if s[i - 1] == "1" or s[i - 1] == "2" and "1" <= s[i] <= "6":
                    fn = fn_1 + fn_2

                else:
                    fn = fn_1
            else:
                if s[i - 1] == "1" or s[i - 1] == "2":
                    fn = fn_2
                else:
                    return 0
            fn_2 = fn_1
            fn_1 = fn
        return fn


print Solution().numDecodings("12")

