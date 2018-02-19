# coding=utf-8
'''
Created on 2017å¹?9æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def dfs(pattern, s, d, rev_d):
            if pattern == s == "":
                return True
            elif pattern == "" or s == "":
                return False
            else:
                if pattern[0] in d:
                    if s.startswith(d[pattern[0]]):
                        return dfs(pattern[1:], s[len(d[pattern[0]]):], d, rev_d)
                    else:
                        return False
                else:
                    for length in xrange(1, len(s) + 1):
                        if s[:length] not in rev_d:
                            d[pattern[0]] = s[:length]
                            rev_d[s[:length]] = pattern[0]
                            if dfs(pattern[1:], s[length:], d, rev_d):
                                return True
                            del d[pattern[0]]
                            del rev_d[s[:length]]
                    return False

        return dfs(pattern, s, {}, {})


pattern = "ab"
s = "aa"
print Solution().wordPatternMatch(pattern, s)

