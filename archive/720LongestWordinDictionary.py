# coding=utf-8
'''
Created on 2017å¹?11æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        d = defaultdict(set)
        maxLen = -1
        for word in words:
            maxLen = max(maxLen, len(word))
            d[len(word)].add(word)
        length = 1
        while d[length]:
            temp = set()
            for word in d[length + 1]:
                if word[:-1] not in d[length]:
                    temp.add(word)
            d[length + 1].difference_update(temp)
            length += 1
        if length > 1:
            return sorted(d[length - 1])[0]
        else:
            return ""


words = ["a"]
print Solution().longestWord(words)

