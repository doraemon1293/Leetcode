# coding=utf-8
'''
Created on 2017å¹?7æœ?13æ—?

@author: Administrator
'''


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        self.d = defaultdict(list)
        for i, word in enumerate(words):
            self.d[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return  min([abs(x - y) for x in self.d[word1] for y in self.d[word2] ])

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
