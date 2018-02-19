# coding=utf-8
'''
Created on 2017å¹?11æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        from collections import defaultdict
        d = defaultdict(set)
        for x, y in pairs:
            d[x].add(y)
            d[y].add(x)
        flag = True
        for i in xrange(len(words1)):
#             print words1[i]
#             print words2[i]
#             print words1[i], d[words1[i]]
            if not (words1[i] == words2[i] or words2[i] in d.get(words1[i], set())):
                flag = False
                break
        return flag


words1 = ["an", "extraordinary", "meal"]
words2 = ["one", "good", "dinner"]
pairs = [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"], ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"], ["actually", "very"], ["really", "very"], ["super", "very"]]

print Solution().areSentencesSimilar(words1, words2, pairs)
