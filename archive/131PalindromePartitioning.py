# coding=utf-8
'''
Created on 2016å¹?12æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == "": return [[]]
        paths = {}
        ans = []
        for i in xrange(len(s)):
            st = en = i
            while st >= 0 and en < len(s) and s[st] == s[en]:
                paths.setdefault(en, set())
                paths[en].add(st)
                st -= 1
                en += 1

            st = i
            en = i + 1
            while st >= 0 and en < len(s) and s[st] == s[en]:
                paths.setdefault(en, set())
                paths[en].add(st)
                st -= 1
                en += 1

        def foo(n, rout):
            if n == -1:
                temp = []
                for st, en in rout[::-1]:
                    temp.append(s[st:en + 1])
                ans.append([s[st:en + 1] for st, en in rout[::-1]])
            else:
                for st in paths[n]:
                    foo(st - 1, rout + [(st, n)])

        foo(len(s) - 1, [])
        return ans


s = "aab"
print Solution().partition(s)

