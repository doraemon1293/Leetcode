# coding=utf-8
'''
Created on 2017å¹?3æœ?29æ—?

@author: Administrator
'''


class Solution(object):

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        abbrs = [(0, "")]

        for ch in word:
            new_abbrs = []
            for n, s in abbrs:
                new_abbrs.append((n + 1, s))
                new_abbrs.append((0, s + (str(n) if n > 0 else "") + ch))
            abbrs = new_abbrs
            print abbrs
        ans = []
        for n, s in abbrs:
            ans.append((s + (str(n) if n > 0 else "")))
        return ans


print Solution().generateAbbreviations("word")

