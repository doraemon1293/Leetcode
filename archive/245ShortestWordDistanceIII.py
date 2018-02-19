# coding=utf-8
'''
Created on 2017å¹?5æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        a1 = []
        a2 = []
        for i, word in enumerate(words):
            if word == word1:
                a1.append(i)
            if word == word2:
                a2.append(i)
        return min([abs(x - y) for x in a1 for y in a2 if y != x])


words = ["a", "b"]
word1 = "a"
word2 = "a"
print Solution().shortestWordDistance(words, word1, word2)
