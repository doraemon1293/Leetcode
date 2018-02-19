# coding=utf-8
'''
Created on 2017å¹?7æœ?4æ—?

@author: Administrator
'''

# coding=utf-8
'''
Created on 2017å¹?7æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict, deque
        d = defaultdict(set)
        if wordList == [] or endWord not in wordList: return 0
        for word in wordList:
            for i in xrange(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                d[s].add(word)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            word, n = q.popleft()
            for i in xrange(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                for word1 in d.get(s, []):
                    if word1 == endWord:
                        return n + 1
                    elif word1 not in visited:
                        visited.add(word1)
                        q.append((word1, n + 1))
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print Solution().ladderLength(beginWord, endWord, wordList)

