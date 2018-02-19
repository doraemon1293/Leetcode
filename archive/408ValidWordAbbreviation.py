# coding=utf-8
'''
Created on 2016å¹?12æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        idx = 0
        num = 0
        abbr += "$"
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == "0":
                    return False
                num = num * 10 + int(c)
            elif c != "$":
                idx += num
                num = 0
                if idx >= len(word) or c != word[idx]:
                        return False
                idx += 1
            else:
                idx += num
                num = 0
                if idx != len(word):
                    return False
        return True


word = "iacb"
abbr = "i3"

print Solution().validWordAbbreviation(word, abbr)
