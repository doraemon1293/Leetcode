# coding=utf-8
'''
Created on 2017年11月27日

@author: Administrator
'''


class Solution(object):

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False

        self.parents = {}
        self.weights = {}

        def find(x):
            if x not in self.parents:
                self.parents[x] = x
                self.weights[x] = 1
                return x
            else:
                path = []
                while self.parents[x] != x:
                    path.append(x)
                    x = self.parents[x]
                for node in path:
                    self.parents[node] = x
                return x

        def union(x, y):
            px = find(x)
            py = find(y)
            heavier = max((self.weights[px], px), (self.weights[py], py))[1]
            for p in (px, py):
                if p != heavier:
                    self.weights[heavier] += self.weights[p]
                    self.parents[p] = heavier

        for x, y in pairs:
            union(x, y)
        # print self.parents

        for i in xrange(len(words1)):
            if find(words1[i]) != find(words2[i]):
                return False
        return True


words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]
print Solution().areSentencesSimilarTwo(words1, words2, pairs)
